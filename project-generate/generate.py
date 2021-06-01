#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年06月01日
 版本:		1.0.0
"""


# Initialize the list
my_list = [1, 3, 6, 10]

"""
生成器
"""
a = (x**2 for x in my_list)

if __name__ == '__main__':
    for g in a:
        print(g)
