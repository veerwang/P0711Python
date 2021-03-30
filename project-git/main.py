#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年03月29日
 版本:		1.0.0
"""


from dulwich.repo import Repo

if __name__ == '__main__':
    r = Repo('.')	
    r.head()
    c = r[r.head()]
    print(c.message.decode('utf-8'))
