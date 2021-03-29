#! /usr/bin/env python3
# coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年09月21日 
# 版本:		1.0.0     

import os

def global_get_version():
    """docstring for global_get_version
    Description: 获取全局模块变量
    Args:
    Returns:
    Raises:
    """
    return 'V1.0.0'

if __name__ == '__main__':
    print("hello the world")
    print( global_get_version.__doc__ )
