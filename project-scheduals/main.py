#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月18日 
# 版本:		1.0.0     

import os
import schedule
import time

def job():
    print("hello the world")

if __name__ == '__main__':
    print("starting ... schedule process")
    myjob = schedule.every(1).seconds.do(job)

    runtime = 0
    while True:
        schedule.run_pending()
        time.sleep(1)
        runtime = runtime + 1 
        if runtime == 3:
            schedule.cancel_job(myjob)
        else:
            print(str(runtime))
