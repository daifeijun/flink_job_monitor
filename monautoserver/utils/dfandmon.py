# coding=utf-8
import requests, json
import pandas as pd
from sqlalchemy import create_engine
import os
from pojo import properties
from utils import apollotest

def getdflist():
    """
    根据sql获取dflist
    :return:
    """
    engine = apollotest.getApolloData('engine')
    engine = create_engine('mysql+pymysql://{0}?charset=utf8'.format(engine))
    selectsql = """
    SELECT
    	jobname,
    	jobtype,
    	statusname,
    	jobowner,
    	jobruncom,
    	detection_time,
    	b.phone
    FROM
    	job_monitor_table a
    LEFT JOIN job_monitor_per b on a.jobowner=b.sname
    WHERE
    	STATUS != 0
    """
    df = pd.read_sql_query(selectsql, con=engine)
    monlist = df.values.tolist()
    return monlist

def monStart(monlist):
    """
    开始告警
    :param monlist:
    :return:
    """
    for row in monlist:
        name = row[3]

        wx_url = apollotest.getApolloData('wx_url')+"="+apollotest.getApolloData('wx_url_e')
        if row[1] == '临时':
            content = '警告：detection_time={3},jobname={0},phone={4},jobstatus={1},jobtype={2}任务,需要相关owner人工排查是否完成或者失败，若失败，请手动执行！！！'.format(
                row[0], row[2], row[1], row[5], row[6])
        else:
            if row[2] == 'FAILED':
                props = apollotest.getApolloData('autopro')
                num = props.get(row[0])
                if num == "":  # 没有查询出内容，加入一
                    props.put(row[0], "1")  # 修改/添加key=value
                else:
                    props.put(row[0], str(1 + int(num)))
                count = props.get(row[0])
                if int(count) <= 10:
                    os.system(row[4])
                    # os.system(row[4])
                    content = '警告：detection_time={4},jobname={0},phone={6},jobstatus={1},jobtype={2}任务,先已开始自动重跑脚本={3},重跑次数{5}次'.format(
                        row[0], row[2], row[1], row[4], row[5], count, row[6])
                else:
                    content = '警告：detection_time={4},jobname={0},phone={6},jobstatus={1},jobtype={2}任务,先已开始自动重跑脚本={3},重跑次数{5}次,不再自动重跑，需要相关owner人工排查！！！'.format(
                        row[0], row[2], row[1], row[4], row[5], count, row[6])
            else:
                content = '警告：detection_time={3},jobname={0},phone={4},jobstatus={1},jobtype={2}任务,此长期任务非FAILED状态，需要相关owner人工排查情况(发现服务轮询期间可能出现job自动恢复正常)！！！'.format(
                    row[0], row[2], row[1], row[5], row[6])
        data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list": [name, "@all"]}})
        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
        print(r.json)
