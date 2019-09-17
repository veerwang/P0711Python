#! /usr/bin/python
#coding=utf-8

#
# 描述:	        添加一种计算执行效率的方法	
# 创建人: 	kevin.wang
# 创建日期:     2019年09月17日 
# 版本:		1.0.0     

import os
import time

def calculate_io_process():
    time.sleep(3)

if __name__ == '__main__':
    startime = time.time()
    calculate_io_process()
    endtime  = time.time()
    print(endtime - startime)
