#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    测试uwsgi
 创建人:	kevin.wang
 创建日期:	2023年03月02日
 版本:		1.0.0
"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    returnstr = 'Hello the world'
    # 关键代码，是要进行encode的编码转换
    return returnstr.encode('utf-8')
