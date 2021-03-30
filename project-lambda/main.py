#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年03月30日
 版本:		1.0.0
"""


import os


if __name__ == '__main__':
    print("hello the world")
    """
    lambda 参数变量: 表达式
    """
    g = lambda x: x + 18
    print(g(10))
    sq = lambda x: x * x
    print(sq(5))
    print(sq(9))
