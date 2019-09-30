#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月30日 
# 版本:		1.0.0     

import os

if __name__ == '__main__':
    print("hello the world")
    a = "hello the world : {version}".format(version='1.0.0')
    print(a)
    a = "hello the world : {:b}".format(11)
    print(a)
    a = "hello the world : {:x}".format(11)
    print(a)
