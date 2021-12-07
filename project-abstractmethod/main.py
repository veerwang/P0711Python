#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    进行抽象基类的实验代码
 创建人:	kevin.wang
 创建日期:	2021年12月07日
 版本:		1.0.0
"""


import os
from abc import ABC, abstractmethod


class BaseServer(ABC):
    """description"""

    def __init__(self):
        pass

    def __del__(self):
        pass

    # 关键代码，这个是一个虚基类的函数
    @abstractmethod
    def dispInfo(self):
        pass


class FTPServer(BaseServer):
    """description"""

    def __init__(self):
        pass

    def __del__(self):
        pass

    # 该函数要被重写，因为基类的函数已经被声明为抽象函数
    def dispInfo(self):
        print('Display FTPServer')


if __name__ == '__main__':
    print("abstract class test")
    ftp = FTPServer()
    ftp.dispInfo()
