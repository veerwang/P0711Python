#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年11月14日 
# 版本:		1.0.0     

import os

def analyze_test(flag):
   print("OK") if flag == 1 else print("BAD")


if __name__ == '__main__':
    analyze_test(1)
    analyze_test(0)
    print("hello the world")
