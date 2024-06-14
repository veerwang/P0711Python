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


# the arguments' type is int or float are both OK
def prj_double(arguments: typing.Union[int, float]):
    return arguments * 2

# Optional[str] = Union[str, None]
def prj_display(arguments: typing.Optional[str]):
    if arguments is not None:
        print(arguments)

if __name__ == '__main__':
    print(prj_double(20))
    prj_display('Hello')
    prj_display(None)
    prj_display(11)
