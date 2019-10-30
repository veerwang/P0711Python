#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月30日 
# 版本:		1.0.0     

import os,time
from commanddef import command 

def dynamic_process_mainline(q):
    while True:
        cmd = q.get(True)
        if cmd.mcmd == 'quit':
            print("dynamic process quit")
            return;
        else:
            print("dynamic process get cmd")
        time.sleep(1)

if __name__ == '__main__':
    print("hello the world")
