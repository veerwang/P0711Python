#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年07月07日
 版本:		1.0.0
"""


import os
import subprocess


if __name__ == '__main__':
    strlist = []
    mystr = ''
    # 以下的设置，是看错误输出信息
    p = subprocess.Popen('task', shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # 以下的设置，是不看错误输出信息
    # p = subprocess.Popen('task', shell=True,
    #                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in p.stdout.readlines():
        # print(str(line, encoding='utf-8'))
        mystr = mystr + str(line, encoding='utf-8')
    retval = p.wait()
    print(mystr)
    strlist = mystr.split('\n')
    for s in strlist:
        print(s)
    print(os.environ)
