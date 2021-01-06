#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from utils import RequestUtil
class ExcutorServer:
    def __init__(self,conn):
        """
        初始化ExcutorServer对象，传入mysql连接
        :param conn: mysql连接
        """
        self.conn=conn

    def findStart(self):
        """
        发现服务启动，先用mysql连接查询所有的jobname，for循环去
        查询，使用linux的yarn命令得到当前的jobname是否为正常状态
        发现不正常状态，则将mysql数据表中的status更新为1(0:running;1:faild)
        """
        conn = self.conn
        # 使用cursor()方法获取操作游标
        cur = conn.cursor()
        # SQL语句查询数据
        sql = "select jobname,jobstatuscom,jobstatuscom1 from job_monitor_table"
        # 执行sql语句
        cur.execute(sql)
        # 得到查询的所有结果
        result = cur.fetchall()
        # 循环进行jobname的状态查询
        for i in range(0, len(result)):
            # 出现查找不到状态则更新mysql中status为1
            self.__process(result[i][0], result[i][1], result[i][2], cur, conn)
        # 关闭游标连接
        cur.close()
        # 关闭数据库连接
        conn.close()

    def __process(self, jobname, command, url, cur, conn):
        """
        先根据yarn application -list |grep jobname命令，返回的值不包含jobname为
        失败，直接更新mysql中状态值为1，状态名为failed，如果有则进行接口调用，出现
        异常情况下，表示appid存在，jobid不存在了，先kill掉appid，执行update操作，
        将mysql对应的jobname的status变为1，如果接口调用成功，得到status的值，则
        将不为RUNNING的更新mysql将mysql对应的jobname的status变为2，job的状态名
        称改为对应的名称
        :param jobname: job名称
        :param command: linux调用命令查看job状态
        :param url: 接口调用地址
        :param cur: 操作游标
        :param conn: mysql连接
        :return:
        """
        if jobname in os.popen(command).read():
            try:
                statusName = RequestUtil.Request(url).getStatusName()
                if statusName == 'RUNNING':
                    self.__update(jobname, cur, conn, 'RUNNING')
                else:
                    self.__update(jobname, cur, conn, statusName)
            except Exception as e:
                    os.system("yarn application -kill "+url.split("/")[4])
                    self.__update(jobname,cur,conn,'exception')
        else:
            self.__update(jobname, cur, conn, 'exception')

    def __update(self,jobname,cur,conn,statusName):
        """
        更新操作，如果status是'exception'表示调用不到接口，则表示此job已failed，就
        将mysql中job status直接改为1，如果调用成功，就将mysql中的job status改为2，
        并将statusname改为现在对应的name
        :param command: linux调用命令查看job状态
        :param cur: 操作游标
        :param conn: mysql连接
        :param status: job状态
        :return:
        """
        if statusName == 'exception':
            # 更新sql，将对应的status改为1
            sql = "update job_monitor_table set status='1',statusname='FAILED' where jobname='%s'" % (jobname)
        elif statusName == 'RUNNING':
            # 更新sql，将对应的status改为0,statusname改为对应的状态名
            sql = "update job_monitor_table set status='0',statusname='RUNNING' where jobname='%s'" % (jobname)
        else:
            sql = "update job_monitor_table set status='2',statusname='%s' where jobname='%s'" % (statusName,jobname)
        # 执行SQL语句
        cur.execute(sql)
        # 提交到数据库执行
        conn.commit()