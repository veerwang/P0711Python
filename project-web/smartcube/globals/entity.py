#! /usr/bin/env python3
# coding=utf-8

"""
 描述:	    单体类的基类
 创建人:	kevin.wang
 创建日期:	2021年03月21日
 版本:		1.0.0
"""


class EntityClass:
    """description"""
    handler = None

    @classmethod
    def getInstance(cls):
        """docstring for getInstance
        Description: 单体实现,可以作为全部的单体类的基类
        Args:
        Returns:
        Raises:
        """
        if cls.handler is None:
            cls.handler = cls()
        return cls.handler
