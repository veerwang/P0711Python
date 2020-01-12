#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年11月25日 
# 版本:		1.0.0     

import os
import time
import subprocess

class processhold:
    def __init__(self,command):
        self.mCmd           = command
        self.mPhandle       = None
        self.mReturnCode    = None

    def __del__(self):
        print('class destroy')

    def start(self):
        self.mPhandle = subprocess.Popen(args=self.mCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True )

    def poll(self):
        if self.mPhandle is not None:
            if self.mPhandle.poll() is not None:
                self.mReturnCode = self.mPhandle.stdout.read()
                return True 
        return False

    def getreturncode(self):
        if self.mReturnCode is not None:
            return self.mReturnCode
        else:
            return 'None'

if __name__ == '__main__':
    print("processhold test start")
    ph = processhold ('./static.py')
    ph.start()
    while(True):
        if ph.poll() == True:
            print('Process finish')
            print(ph.getreturncode())
            break;
        else:
            time.sleep(1)

