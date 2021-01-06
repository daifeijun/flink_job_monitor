# coding=utf-8
import requests, json
import datetime
import pandas as pd
from sqlalchemy import create_engine
from utils import timeutil
from utils import apollotest

xq=timeutil.get_week_day(datetime.datetime.now())
engine = apollotest.getApolloData('engine')
engine = create_engine('mysql+pymysql://{0}?charset=utf8'.format(engine))

selectsql = """
select
`name`,sname,phone
from job_monitor_per
where dutydate='{0}'
""".format(xq)
df = pd.read_sql_query(selectsql, con=engine)
dflist=df.values.tolist()
print(dflist)
name=dflist[0][1]
content='温馨提示：今天={0}，值班人员={1}，值班人员电话号码={2}，值班时间段=[当天早9：00~第二天早9：00]，请务必保证值班当天电话畅通&企业微信在线！！！'.format(xq,dflist[0][0],dflist[0][2])
wx_url =apollotest.getApolloData('wx_url')

data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list": [name, "@all"]}})
r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
print(r.json)
