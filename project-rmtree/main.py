#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年11月18日 
# 版本:		1.0.0     

import os
import shutil

if __name__ == '__main__':
    path = 'testdir'
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("mkdir " + path)

    try:
        shutil.rmtree("fff")
    except Exception as e:
        print(e)

    print("hello the world")
