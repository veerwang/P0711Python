#! /usr/bin/env python3
# coding=utf-8

"""
 description:
 author:		kevin.wang
 create date:	2024-06-14
 version:		1.0.0
"""


import os

import typing

def Display(arguments: typing.Callable):
    """docstring for Display
    Description:
    Args:
    Returns:
    Raises:
    """
    arguments()

def SayHello():
    print('Say Hello')
    

if __name__ == '__main__':
    Display(SayHello)
