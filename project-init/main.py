#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月29日 
# 版本:		1.0.0     

import os
import libutils.mythread
import libutils

if __name__ == '__main__':
    print("hello the world")
    print('version: ' + libutils.mythread.get_version() )
    print('Exutils Version: ' + libutils.Exutils.get_exutils_version())
