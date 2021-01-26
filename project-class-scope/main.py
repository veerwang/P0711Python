#! /usr/bin/env python3
#coding=utf-8

"""
 描述:		工程测试		 
 创建人:	kevin.wang
 创建日期:	2021年01月26日 
 版本:		1.0.0     
"""
import os

class Human():
    # 这种变量属于类变量
    ghost = True
    """docstring for Human"""
    def __init__(self, name):
        # 这种变量属于实例变量，要采用这种方式初始化
        self.name = name

    def __del__(self):
        print("kill " + self.name)

if __name__ == '__main__':
    print("进行类变量，实例变量的实验")
    he = Human("kevin")
    she = Human("rita")
    print("doing something")
    he.ghost = False
    print(he.ghost)
    print("doing something")
    print(Human.ghost)
    Human.ghost = False
    print(she.ghost)
