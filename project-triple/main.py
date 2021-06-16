#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    Triple返回值的测试，可以认为为list
 创建人:	kevin.wang
 创建日期:	2021年06月16日
 版本:		1.0.0
"""


def returnTriple():
    """docstring for returnTriple
    Description:
    Args:
    Returns:
    Raises:
    """
    return (1, 12, 2021)


if __name__ == '__main__':
    result = returnTriple()
    print(result[1])
