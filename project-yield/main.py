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
    # 由于函数当中有yield关键字，不会被执行
    # 只是将函数对象赋值给g
    g = Fun_A()
    # next(g) 会执行到yield i 返回，即返回 0
    # 即打印 0
    print(next(g))
    # 继续执行result是none,没有内容
    # 之后返回 1
    print(next(g))
    # send(100)标示 将yield i 中的 i赋值为100
    g.send(100)
    print(next(g))
