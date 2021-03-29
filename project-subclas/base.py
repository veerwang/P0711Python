#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年03月29日
 版本:		1.0.0
"""


import os

class Base:
    def __init__(self):
        self.name = 'kevin'

    def __del__(self):
        pass

    def dispName(self):
        print(self.name)
