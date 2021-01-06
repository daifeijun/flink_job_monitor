from pojo import properties
import requests
from utils import proutils,apollotest
import os
# def getvaluebykey(key):
#     props = properties.Properties("/home/bdrdus/flink_job_monitor/env.properties")
#     #props = properties.Properties(r"C:\Users\Administrator\Desktop\env.properties")
#     return props.get(key)


def getjobidornot(jobname):
    with open('{1}/{0}.log'.format(jobname,apollotest.getApolloData('logdir')),'r') as fp:
        read = fp.read()
        if 'JobID' in read:
            return True
        else:
            return False
def rmjoblog(jobname):
    os.remove('{1}/{0}.log'.format(jobname,apollotest.getApolloData('logdir')))

def getyarncode():
    try:
        yarn = apollotest.getApolloData('yarn')
        res = requests.get(yarn)
        code=res.status_code
    except Exception as e:
        code = 500
    return  code

if __name__ == '__main__':
    jobidornot = getjobidornot('devicestatusmqodsname')
    print(jobidornot)
