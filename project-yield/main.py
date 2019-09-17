#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试
# 创建人: 	kevin.wang
# 创建日期:     2019年09月17日 
# 版本:		1.0.0

import os

def Fun_A():
    for i in range(4):
        result = yield i
        print("i value: " + str(result))

if __name__ == '__main__':
    print("the programe is for yiled")
    g = Fun_A()
    print(next(g))
    print(next(g))
    g.send(100)
    print(next(g))
