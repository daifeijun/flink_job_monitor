#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
class DataBase:

    def __init__(self,host,port,user,passwd,dbname):
        """
        初始化数据库连接对象，传入ip，端口号等属性
        :param host: ip地址
        :param port: 端口号
        :param user: 用户名
        :param passwd: 密码
        :param dbname: 数据库名
        """
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.dbname=dbname

    def getConn(self):
        """
        已初始化好的对象，返回connect连接
        :return: conn
        """
        conn = pymysql.connect(
            host=self.host,  # 数据库名
            port=self.port,  # 端口
            user=self.user,  # 用户
            passwd=self.passwd,  # 密码
            db=self.dbname,  # 数据库名称
            charset='utf8'  # 编码方式
        )
        return conn

