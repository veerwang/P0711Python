#! /usr/bin/python
#coding=utf-8

import sqlite3
import logging

def init_log():
    logging.basicConfig(filename='debug.log',level=logging.INFO)

def init_sqlite_database():
    # 创建一个数据库
    conn   = sqlite3.connect("mytest.db")
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

def project_test():
    conn   = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute('select * from adminexcel')
    result = cursor.fetchall()
    # 打印查询结果
    print(result)
    cursor.execute("create table if not exists "+"kevin"+"excel (id varchar(20) primary key NOT NULL,idcode text NOT NULL,describe text NOT NULL,Abscissa text NOT NULL,Ordinate text NOT NULL)")
    for i in range(len(result)):
        c.execute('update '+'kevin'+'excel set idcode = ?,describe = ?,Abscissa=?,Ordinate=? where Ordinate = ?',(result[i]["idcode"],result[i]["describe"],result[i]["Abscissa"],result[i]["Ordinate"],result[i]["oldOrdinate"]))
    conn.commit()
    cursor.close()
    conn.close()

def read_table():
    conn   = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute('select * from kevinexcel')
    result = cursor.fetchall()
    # 打印查询结果
    print(result)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    print("sqlite3 database test")
    init_log()

    try:
        #init_sqlite_database()
        #project_test()
        read_table()
    except Exception as e:
        logging.info("kevin -->")
        logging.info(e) 
