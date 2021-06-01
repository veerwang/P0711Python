#! /usr/bin/env python3
#coding=utf-8

#
# 描述:	        添加一种计算执行效率的方法	
# 创建人: 	kevin.wang
# 创建日期:     2019年09月17日 
# 版本:		1.0.0     

import os
import time
import datetime

def calculate_io_process():
    time.sleep(1)

def print_time():
    ntime = datetime.datetime.strptime("2022 17:22:00","%Y %H:%M:%S")
    print(ntime)


if __name__ == '__main__':
    startime = time.time()
    calculate_io_process()
    endtime  = time.time()
    print(endtime - startime)
    print_time()
