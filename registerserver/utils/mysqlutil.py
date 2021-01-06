# coding=utf-8
import pandas as pd
import time
from sqlalchemy import create_engine
from utils import proutils,apollotest
def getEngine():
    """
    获取engin
    :return:
    """
    engine = apollotest.getApolloData('engine')
    engine = create_engine('mysql+pymysql://{0}?charset=utf8'.format(engine))
    return engine

def getjobrunornot(jobname):
    selectsql = """
    select jobname from job_monitor_table where jobname='{0}' and status=0
    """.format(jobname)
    querydf = pd.read_sql_query(selectsql, con=getEngine())
    return querydf.empty

def  registerMonTab(jobname,jobtype,status,statusname,jobowner,jobstatuscom,jobstatuscom1,jobruncom):
    """
    注册信息到监控表，根据jobname先delete再insert
    :param jobname:任务名称
    :param jobtype:任务类型
    :param status:任务状态
    :param statusname:任务状态名称
    :param jobowner:任务owner
    :param jobstatuscom:任务运行状态命令
    :param jobstatuscom:任务运行状态api
    :param jobruncom:
    :return:
    """
    try:
        deletesql="""
        delete from job_monitor_table where jobname='{0}'
        """.format(jobname)
        print(deletesql)
        pd.read_sql_query(deletesql,con=getEngine())
    except Exception as e:
        insertsql="""
        insert into job_monitor_table(jobname,jobtype,status,statusname,jobowner,jobstatuscom,jobstatuscom1,jobruncom) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')
        """.format(jobname,jobtype,status,statusname,jobowner,jobstatuscom,jobstatuscom1,jobruncom)
        print(insertsql)
        try:
            pd.read_sql_query(insertsql,con=getEngine())
        except Exception as e:
            pass

