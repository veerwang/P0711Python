#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	        最原始的装饰器的使用
 创建人:	kevin.wang
 创建日期:	2021年04月12日
 版本:		1.0.0
"""


def Log(Fun):
    def Wraper():
        print("Loger display ..." + Fun.__name__)
        return Fun()
    return Wraper


@Log
def normalFun():
    print("this is a normal function")


if __name__ == '__main__':
    normalFun()
    print("函数的名称被改变了，由Wraper去替换了-->" + normalFun.__name__)
