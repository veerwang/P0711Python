#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月12日 
# 版本:		1.0.0     

import os

def init_file():
    print("init file")

class Global():
    def __init__ (self,id):
        print("init")
        self.id = id

    def __del__ (self):
        print("del")

    def showme(self):
        print("id: " + str(self.id))

if __name__ == '__main__':
    print("hello the world")
