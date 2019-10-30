#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月30日 
# 版本:		1.0.0     

import os,time

# 注意不同进程之间变量是不能够，通过全局变量访问的。
g_value = 10

def static_process_mainline(q):
    time.sleep(1)
    q.put(g_value+1)
    time.sleep(1)
    q.put(g_value)

def dynamic_process_mainline(q):
    g_value = 1000
    g_value = q.get(True) 
    print("value " + str(g_value))
    g_value = 100
    time.sleep(1)
    g_value = q.get(True) 
    print("value " + str(g_value))

if __name__ == '__main__':
    print("hello the world")
