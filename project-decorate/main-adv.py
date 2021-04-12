#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	        添加functools.wrapers,保证函数信息没有被替换
 创建人:	kevin.wang
 创建日期:	2021年04月12日
 版本:		1.0.0
"""

from functools import wraps


def Log(Fun):
    @wraps(Fun)
    def Wraper(*args, **kwargs):
        print("Advance Loger Display ...")
        return Fun(*args, **kwargs)
    return Wraper


@Log
def normalFun():
    print("this is a normal function")


if __name__ == '__main__':
    normalFun()
    print("函数的名称没有被替换了-->" + normalFun.__name__)
