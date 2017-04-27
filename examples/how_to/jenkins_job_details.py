# -*- coding: cp936 -*-
"""
输入：jenkins job名称和日期(年、年-月、年-月-日)
输出：job的名称、日期、执行次数、成功次数、失败次数、未执行次数、不稳定次数
"""
import datetime, time
from jenkinsapi.jenkins import *
from jenkinsapi.job import *
from jenkinsapi.build import Build


def Get_Date_List(Job_Name):
    my_job = jenkins.get_job(Job_Name)
    first_build = my_job.get_first_buildnumber()  # 获得jenkins列表中的第一个构建数目，不一定是从1开始的
    last_build = my_job.get_last_buildnumber()  # 获得最近一次构建的数目

    for count in xrange(first_build, last_build + 1):  # 依次获得每一个job号
        count_build = my_job.get_build(count)
        start_time = count_build.get_timestamp()  # 获得构建时间，时区好像不大对

        adjust_time = start_time + datetime.timedelta(hours=8)  # 所以在这里加了8小时，变成北京时间了
        Build_Time = adjust_time.strftime("%Y-%m-%d")  # 输出时间的格式
        Status = count_build.get_status()  # 返回这次构建的状态，成功或失败

        print my_job, count, Build_Time, Status


if __name__ == "__main__":
    jenkins = Jenkins('http://10.167.210.237:8081/', 'panwei', '666666')
    Job_Name = 'chp-job'
    Get_Date_List(Job_Name)