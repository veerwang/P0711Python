#! /usr/bin/env python3
# coding=utf-8

"""
 描述:		工程测试
 创建人:	kevin.wang
 创建日期:	2021年10月25日
 版本:		1.0.0
"""

import os
import contextvars


def Main():
    print(os.system("env"))


if __name__ == '__main__':
    print("Test Context function")
    pwd_var = contextvars.ContextVar('PWD')
    pwd_var.set("/home/kevin/rita")

    ctx = contextvars.copy_context()
    print(ctx[pwd_var])
    ctx.run(Main)
