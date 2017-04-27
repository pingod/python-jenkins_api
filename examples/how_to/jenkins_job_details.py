# -*- coding: cp936 -*-
"""
���룺jenkins job���ƺ�����(�ꡢ��-�¡���-��-��)
�����job�����ơ����ڡ�ִ�д������ɹ�������ʧ�ܴ�����δִ�д��������ȶ�����
"""
import datetime, time
from jenkinsapi.jenkins import *
from jenkinsapi.job import *
from jenkinsapi.build import Build


def Get_Date_List(Job_Name):
    my_job = jenkins.get_job(Job_Name)
    first_build = my_job.get_first_buildnumber()  # ���jenkins�б��еĵ�һ��������Ŀ����һ���Ǵ�1��ʼ��
    last_build = my_job.get_last_buildnumber()  # ������һ�ι�������Ŀ

    for count in xrange(first_build, last_build + 1):  # ���λ��ÿһ��job��
        count_build = my_job.get_build(count)
        start_time = count_build.get_timestamp()  # ��ù���ʱ�䣬ʱ�����񲻴��

        adjust_time = start_time + datetime.timedelta(hours=8)  # �������������8Сʱ����ɱ���ʱ����
        Build_Time = adjust_time.strftime("%Y-%m-%d")  # ���ʱ��ĸ�ʽ
        Status = count_build.get_status()  # ������ι�����״̬���ɹ���ʧ��

        print my_job, count, Build_Time, Status


if __name__ == "__main__":
    jenkins = Jenkins('http://10.167.210.237:8081/', 'panwei', '666666')
    Job_Name = 'chp-job'
    Get_Date_List(Job_Name)