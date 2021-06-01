#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年06月01日
 版本:		1.0.0
"""


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


if __name__ == '__main__':
    # For loop to reverse the string
    for char in rev_str("hello"):
        print(char)
