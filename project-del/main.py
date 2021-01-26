#! /usr/bin/env python3
#coding=utf-8

"""
 描述:	    实验del的关键字的用法	
 创建人:	kevin.wang
 创建日期:	2021年01月26日 
 版本:		1.0.0     
"""

import os

class BaseClass():
    """docstring for BaseClass"""
    def __init__(self):
        print("create")

    def __del__(self):
        print("destroy")

if __name__ == '__main__':
    a = ['a',2,'b',"hello"]
    print(a)
    del a[2]    # 删除'b'元素
    print(a)
    bc = BaseClass()
    del bc
