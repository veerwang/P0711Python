#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    时间间隔的测试代码	
 创建人:	kevin.wang
 创建日期:	2021年09月30日
 版本:		1.0.0
"""


import datetime


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    tdate = '2021-10-30'
    ttime = '14:40:00'
    newTime = datetime.datetime.strptime(
        tdate + ' ' + ttime, '%Y-%m-%d %H:%M:%S')

    if newTime - startTime > datetime.timedelta(minutes=1):
        print('OK1')

    if newTime - startTime > datetime.timedelta(seconds=10):
        print('OK2')
