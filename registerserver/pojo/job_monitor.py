# coding=utf-8
from utils import mysqlutil as mt
import os
from utils import proutils,apollotest

class job_monitor_table:
    def __init__(self, jobname, jobtype, jobowner,jobruncom):
        """
        构造方法
        :param jobname:
        :param jobtype:
        :param jobowner:
        :param jobruncom:
        """
        self.jobname = jobname
        self.jobtype = jobtype
        self.status = '0'
        self.statusname='RUNNING'
        self.jobowner = jobowner
        self.jobstatuscom = 'yarn application -list | grep %s' % jobname
        self.jobruncom = jobruncom

    def getappidAjobid(self):
        """
        根据yarn application -list | grep xxxx 得到appid
        根据xxx.log 得到jobid
        最后得到
        :return:jobstatuscom1
        """
        appid = os.popen(self.jobstatuscom).read().splitlines()[0]
        yarn = apollotest.getApolloData('yarn')
        jobstatuscom1='{1}/proxy/{0}/jobs/overview'.format(appid.split()[0],yarn)
        return jobstatuscom1

    def registerStart(self):
        """
        调取注册函数
        :return:
        """
        jobstatuscom1=self.getappidAjobid()
        mt.registerMonTab(self.jobname, self.jobtype, self.status, self.statusname,self.jobowner,self.jobstatuscom, jobstatuscom1,self.jobruncom)

