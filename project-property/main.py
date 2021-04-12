#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	        属性装饰器的使用
 创建人:	kevin.wang
 创建日期:	2021年04月12日
 版本:		1.0.0
"""


import os


class Study:
    """description
    """

    def __init__(self):
        self._name = 'kevin'
        pass

    def __del__(self):
        pass

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name


if __name__ == '__main__':
    person = Study()
    print(person.Name)
    person.Name = 'wangwei'
    print(person.Name)
