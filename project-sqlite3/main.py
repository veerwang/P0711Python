#! /usr/bin/python
#coding=utf-8

import sqlite3
import logging

def init_log():
    logging.basicConfig(filename='debug.log',level=logging.INFO)

def init_sqlite_database():
    # 创建一个数据库
    conn   = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'1\', \'Kevin\')')
    cursor.execute('select * from user where id=?', '1')

    result = cursor.fetchall()
    # 打印查询结果
    print(result)

    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("sqlite3 database test")
    init_log()

    try:
        init_sqlite_database()
    except Exception as e:
        print("kevin -->")
        logging.info(e) 
