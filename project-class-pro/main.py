#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2021年01月07日 
# 版本:		1.0.0     

import os

class base:
    _name = ["kevin","wangwei"]

    def __init__(self):
        pass

    def __del__(self):
        print("base destroy")

    def name(self):
        print(self._name)

    #
    # 核心代码，类静态函数
    #
    @staticmethod
    def static_fun():
        print("static function")

if __name__ == '__main__':
    print("类的多态的实现")
    b = base()
    b.name()
    base.static_fun()
