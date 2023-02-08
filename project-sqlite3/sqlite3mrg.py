#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试
# 创建人:	kevin.wang
# 创建日期:     2019年11月15日
# 版本:		1.0.0

import os
import sqlite3


# 运行数据库的语句
def database_get_data(database,cmd):
    try:
        conn   = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(cmd)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print('except...', e)
    else:
        return result
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    print("hello the world")
