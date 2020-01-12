#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月30日 
# 版本:		1.0.0     

import os,time,random
import globalvariables as gv
import static_process as sp
import dynamic_process as dp

from commanddef import command 

from multiprocessing import Process,Queue

def init_processes():
    gv.process_queue            = Queue()
    gv.static_process_handle    = Process(target=sp.static_process_mainline, args=(gv.process_queue,))
    gv.dynamic_process_handle   = Process(target=dp.dynamic_process_mainline, args=(gv.process_queue,))

def start_processes():
    gv.static_process_handle.start()
    gv.dynamic_process_handle.start()

def wait_processes():
    gv.static_process_handle.join()
    gv.dynamic_process_handle.join()

if __name__ == '__main__':
    init_processes()
    start_processes()

    # 注意他这个命令可能被其他进程截获
    cmd = command()
    cmd.mcmd = 'send'
    gv.process_queue.put(cmd)
    wait_processes()
