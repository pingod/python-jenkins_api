# -*- coding: gb2312 -*-
"""
���룺jenkins�������ĵ�ַ���û���������
������Ѷ����job���б�
"""
import datetime, time
from jenkinsapi.jenkins import *
from jenkinsapi.job import *
from jenkinsapi.build import Build
def Url_Get_Job_List(url='http://10.167.210.237:8081/', username='panwei', password='666666'):
    jenkins = Jenkins(url, username, password)
    count = 0
    for job_name in jenkins.keys():
        my_job = jenkins.get_job(job_name)
        count = count + 1
        print "Job" + str(count) + " : "+job_name
if __name__ == "__main__":
    Url_Get_Job_List()