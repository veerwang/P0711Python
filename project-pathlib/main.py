#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月18日 
# 版本:		1.0.0     

import os
import sys
import pathlib

def usage():
    print("Uage: main.py write/read")

if __name__ == '__main__':
    print("文件操作工程")

    if len(sys.argv) == 2:
        if  sys.argv[1] == 'write':
            p = pathlib.Path('run.log')
            f = p.open('a')
            f.write('first line\n')
            f.write('second line\n')
            f.write('third line\n')
        elif sys.argv[1] == 'read':
            p = pathlib.Path('run.log')
            print(p.read_text())
    else:
        usage()
