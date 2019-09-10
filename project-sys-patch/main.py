#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月07日 
# 版本:		1.0.0     

import os
import sys

if __name__ == '__main__':
   sys.path.append('/home/kevin/github/P0711Python/project-lib') 
   import libmanager 
   print('version: ' + libmanager.getVersion() )
