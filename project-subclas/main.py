#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年03月29日
 版本:		1.0.0
"""


import os
from base import Base

class Object(Base):
    def __init__(self):
        Base.__init__(self)

    def __del__(self):
        pass

if __name__ == '__main__':
    print("hello the world")
    obj = Object()
    obj.dispName()
