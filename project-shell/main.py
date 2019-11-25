#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年11月20日 
# 版本:		1.0.0     

import os
import time
import subprocess

def test(size,file): 
    print('start')
    #cmd = 'dd if=/dev/urandom bs=1 count=%d 2>%s' % (size,file) 
    cmd = './static.py'
    #p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True) 
    p = subprocess.Popen(args=cmd, shell=True, stderr=subprocess.STDOUT, close_fds=True )
    os.system('./static.py')

    while p.poll() is None:
        print('sleeping')
        time.sleep(1)

if __name__ == '__main__':
    print("this is main thread")
    for i in range(3):
        test(1024*100,i)
