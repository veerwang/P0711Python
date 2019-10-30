#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月30日 
# 版本:		1.0.0     

import os

# 进行进程间命令传递的变量
class command:
    def __init__(self):
        self.mcmd = None
        print("class create")
    def __del__(self):
        self.mcmd = None
        print("class destroy")

if __name__ == '__main__':
    print("hello the world")
