#! /usr/bin/python
#coding=utf-8

#
# 本程序用于实验tuple程序
#
#

import os

def g_tuple_fun(x,y):
    return x + y, x * y


def main():
    t = g_tuple_fun(10,20)
    print("first return value = " + str(t[0]))
    print("second return value = " + str(t[1]))


if __name__ == '__main__':
    main()
