#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年07月26日
 版本:		1.0.0
"""


import os
import ctypes


if __name__ == '__main__':
    print("python call C++ library")
    solib = ctypes.cdll.LoadLibrary(os.getcwd() + "/libutils.so.0.0")
    version = solib.getVersion()
    print(version)
    print(solib.addAlgorithm(10, 20))
    print(solib.getFlag(20))
    print(solib.getFlag(9))

    # 该语句非常重要
    solib.dispName.restype = ctypes.c_char_p

    s = "wangwang"
    news = solib.dispName(bytes(s, 'utf-8'))
    print(str(news, 'utf-8'))
