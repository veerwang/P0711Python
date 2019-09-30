#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月30日 
# 版本:		1.0.0     

import os
import pathlib

def search_string(filepath,strvalue):
    p = pathlib.Path(filepath)
    if p.exists():
        with open(filepath,'r') as fhandler:
            while True:
                line = fhandler.readline()
                if line:
                    if strvalue in line:
                        print("find it out")
                else:
                    break


if __name__ == '__main__':
    search_string('api','OnDoubleTap')
   
