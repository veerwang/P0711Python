#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月29日 
# 版本:		1.0.0     

import os
import libutils.mythread
import libutils

if __name__ == '__main__':
    print("hello the world")
    print('version: ' + libutils.mythread.get_version() )
    # 注意此处的用法，Exutils是在libutils模块中的init.py文件中被导入，虽然有下一级的模块，但是
    # 由于导入了，因此只要在libutils模块中引用即可
    print('Exutils Version: ' + libutils.Exutils.get_exutils_version())
