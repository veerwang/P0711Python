#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年06月11日
 版本:		1.0.0
"""


import requests


if __name__ == '__main__':
    r = requests.get('http://www.weather.com.cn/data/cityinfo/101230201.html')
    r.encoding = 'utf-8'
    print(
        r.json()['weatherinfo']['city'],
        r.json()['weatherinfo']['ptime'],
        r.json()['weatherinfo']['weather'],
        r.json()['weatherinfo']['temp1'],
        r.json()['weatherinfo']['temp2'])
