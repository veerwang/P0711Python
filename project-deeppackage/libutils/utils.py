#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月15日 
# 版本:		1.0.0     

import os
import libsubmodules.submodules

def getModuleVersion():
    return libsubmodules.submodules.getSubModules() 


if __name__ == '__main__':
    print("hello the world")
