#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	        带参数的装饰器 
 创建人:	kevin.wang
 创建日期:	2021年04月12日
 版本:		1.0.0
"""

from functools import wraps


def Log(level):
    def Mid(Fun):
        @wraps(Fun)
        def Wraper(*args, **kwargs):
            print("Advance Loger Display ..." + str(level))
            return Fun(*args, **kwargs)
        return Wraper
    return Mid


@Log(level=1)
def normalFun(name):
    print("this is a normal function " + name)


if __name__ == '__main__':
    normalFun("wangwei")
    print("函数的名称没有被替换了-->" + normalFun.__name__)
