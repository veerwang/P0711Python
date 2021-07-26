#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年07月26日
 版本:		1.0.0
"""


import os
from ctypes import *


if __name__ == '__main__':
    print("python call C++ library")
    solib = cdll.LoadLibrary(os.getcwd()+ "/libutils.so.0.0")
    version = solib.getVersion()
    print(version)
    print(solib.addAlgorithm(10,20))
    print(solib.getFlag(20))
    print(solib.getFlag(9))
