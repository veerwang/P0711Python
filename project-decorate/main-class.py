#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	        类装饰器的使用
 创建人:	kevin.wang
 创建日期:	2021年04月12日
 版本:		1.0.0
"""


class Log():
    """description
    """

    def __init__(self, func):
        self._func = func

    def __call__(self):
        print("decorate start")
        self._func()
        print("decorate end")


@Log
def normalFun():
    print("this is a normal function")


if __name__ == '__main__':
    normalFun()
