#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月30日 
# 版本:		1.0.0     

import os,time,random
import globalvariables as gv
import analyze_process as ap

from multiprocessing import Process,Queue

def init_processes():
    gv.process_queue            = Queue()
    gv.static_process_handle    = Process(target=ap.static_process_mainline, args=(gv.process_queue,))
    gv.dynamic_process_handle   = Process(target=ap.dynamic_process_mainline, args=(gv.process_queue,))

def start_processes():
    gv.static_process_handle.start()
    gv.dynamic_process_handle.start()

def wait_processes():
    gv.static_process_handle.join()
    gv.dynamic_process_handle.join()

if __name__ == '__main__':
    init_processes()
    start_processes()
    wait_processes()
