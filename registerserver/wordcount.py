# coding=utf-8
from pojo import job_monitor
import time
import subprocess
from utils import proutils
from utils import mysqlutil
if __name__=="__main__":
    # code = proutils.getyarncode()
    while proutils.getyarncode()!=200:
        print('CHD环境正在启动中。。。')
        time.sleep(1)
    else:
        print('已经成功链接到CHD环境，正在启动job。。。')
        time.sleep(1)

    #个人填写部分  文件名=-ynm 项目名 =jobname =日志文件名方便今后程序获取jobid
    # jobrun='dir'
    jobrun=''
    jobname=''
    jobtype='长期'#长期&临时
    jobowner=''#拼音
    jobruncom='sudo python3 /home/bdrdus/flink_job_monitor/registerserver/.py'#与文件名
    # 个人填写部分
    if mysqlutil.getjobrunornot(jobname):
        p = subprocess.Popen(jobrun, shell=True)
        while(True):
            time.sleep(1)
            if proutils.getjobidornot(jobname):
                print('job ok')
                jm=job_monitor.job_monitor_table(jobname=jobname,jobtype=jobtype,jobowner=jobowner,jobruncom=jobruncom)
                jm.registerStart()
                proutils.rmjoblog(jobname)
                p.kill()
                break
            else:
                print('job 启动中，请稍等。。。')
    else:
        print('{0}此job已经运行和注册，请不要重复执行！！！'.format(jobname))


