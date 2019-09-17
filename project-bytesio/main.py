#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月17日 
# 版本:		1.0.0     

import os
from io import BytesIO

if __name__ == '__main__':
    print("hello the world")
    f = BytesIO()
    f.write(b'hello')
    f.write(b' ')
    f.write(b'world')

    f.write('中文'.encode('utf-8'))
    print(f.getvalue())
