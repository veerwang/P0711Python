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

def Onejob():
    print("1 seconds task")

def Twojob():
    print("2 seconds task")

if __name__ == '__main__':
    print("starting ... schedule process")
    myjob = schedule.every(1).seconds.do(Onejob)
    sejob = schedule.every(2).seconds.do(Twojob)
    sejob.tag("sejob")

    runtime = 0
    while True:
        schedule.run_pending()
        time.sleep(1)
        runtime = runtime + 1 
        if runtime == 4:
            schedule.cancel_job(myjob)
        elif runtime == 6:
            schedule.clear("sejob")
        else:
            print(str(runtime))
