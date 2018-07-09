#! /usr/bin/python
#coding=utf-8

#
# 本工程用于测试我重新开始学习的python语言
#  该程序的功能是进行二进制文件的调整
#

#from utils import g_print_version
import utils
import os

if __name__ == '__main__':
    utils.g_print_version()           #本行语句需要紧紧连着上一条语句
    utils.g_print_os_info()
    outstr1 = str(type(12.6))
    print(outstr1)

    utils.g_do_print_times(5)

    t = utils.g_tuple_return(2,4) 
    print(t[0])
    print(t[1])
