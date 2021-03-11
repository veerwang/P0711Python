#! /usr/bin/env python3
#coding=utf-8

"""
 描述:		工程测试		 
 创建人:	kevin.wang
 创建日期:	2021年03月11日 
 版本:		1.0.0     
"""

import os

def modify_list_info(objlist):
    """docstring for modify_list_info
    Description: 如果是列表也是传地址的
    Args:
    Returns:
    Raises:
    """
    print("in -->" + objlist[0])
    print("in -->" + objlist[1])

    objlist[0] = 'dog'
    objlist[1] = 'pig'
    
def modify_dict_info(obj):
    """docstring for modify_
    Description: 如果是字典则是传地址的
    Args:
    Returns:
    Raises:
    """
    print("in -->" + obj[1])
    obj[1] = 'wwei'

if __name__ == '__main__':
    obj = {1:'kevin'}
    print("out -->" + obj[1])
    modify_dict_info(obj)
    print("out -->" + obj[1])
    print('----------------------')
    objlist = ['1','2','3','4']
    print("out -->" + objlist[0])
    print("out -->" + objlist[1])
    modify_list_info(objlist)
    print("out -->" + objlist[0])
    print("out -->" + objlist[1])
