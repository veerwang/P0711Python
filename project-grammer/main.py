#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月11日 
# 版本:		1.0.0     

import os
import utils.fileopt as FileOpt
from utils.fileopt import Global

def yield_test(mylist):
    for ml in mylist:
        yield ml + 2
        print("aa")

if __name__ == '__main__':
    print("hello the world")
    mylist = [1,2,3,4]
    newlist = yield_test(mylist)
    print("bb")
    for aa in newlist:
        print(aa)
        print("cc")

    FileOpt.init_file()

    myglobal = Global("cve")
    myglobal.showme()
