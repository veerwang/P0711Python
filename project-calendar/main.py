#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年06月09日
 版本:		1.0.0
"""


import datetime
import calendar


if __name__ == '__main__':
    # 星期一为第一天
    calendar.setfirstweekday(0)

    # calendar(year, w=2, l=1, d=3, n=6)
    # w: 每个日期两个字符，一般年都是2
    # l: 每行显示几行,一般都是1
    # d: 月与月的间隔
    # n: 每行显示几个月
    # result = calendar.calendar(datetime.datetime.now().year, 2, 1, 3, 1)
    result = calendar.month(datetime.datetime.now().year, 6, 2, 1)
    strlist = result.split('\n')
    for i in range(len(strlist)):
        print(strlist[i])
