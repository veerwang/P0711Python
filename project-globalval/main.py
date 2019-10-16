#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月16日 
# 版本:		1.0.0     

import os

g_version_id = 10

def local_variables():
    local_variable = 'wangwei'

    def nolocal_variables():
        # 这样以下的函数局部变量就可以被修改了
        nonlocal local_variable
        local_variable = 'veer'

    nolocal_variables()
    print(local_variable)

def modify_valriabl():
    # 说明一下使用的g_version_id是全局变量
    global g_version_id
    g_version_id = 2

if __name__ == '__main__':
    print("hello the world")
    modify_valriabl()
    print(g_version_id)
    local_variables()
