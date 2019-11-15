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
    cursor.execute("create table if not exists "+"veer"+"excel (id varchar(20) primary key NOT NULL,idcode text NOT NULL,describe text NOT NULL,Abscissa text NOT NULL,Ordinate text NOT NULL)")
    length = len(result)
    print(str(length))
    try:
        for i in range(length):
            print("kevin")
            #c.execute('update '+'veer'+'excel set idcode = ?,describe = ?,Abscissa=?,Ordinate=? where Ordinate = ?',(result[i][1],result[i][2],result[i][3],result[i][4],result[i][5]))
            data = " 1,\'1\',\'happy\',\'world\',\'fast\' " 
            c.execute('INSERT INTO '+'veerexcel VALUES(%s)' % data)
    except Exception as e:
        logging.info(e) 
    conn.commit()
    cursor.close()
    conn.close()

def read_table():
    conn   = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute('select * from veerexcel')
    result = cursor.fetchall()
    # 打印查询结果
    print(result)

    cursor.close()
    conn.close()

#### 数据库测试代码
def database_operator_init(name,value):
    # 创建一个数据库
    conn   = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        cursor.execute('create table veertable (id varchar(20) primary key NOT NULL,idcode text NOT NULL,describe text NOT NULL,Abscissa text NOT NULL,Ordinate text NOT NULL)')
        cursor.execute('insert into ' + name + 'table (id, idcode, describe, Abscissa, Ordinate)' + ' values (%d, "%s","%s","%s","%s")' %(1,'kevin','test','file',value))
        cursor.execute('insert into ' + name + 'table (id, idcode, describe, Abscissa, Ordinate) values ("2", "Veer","happy","16","5")')
        cursor.execute('select * from ' + name + 'table')
    except BaseException as e:
        print('except...', e)
    else:
        result = cursor.fetchall()
        # 打印查询结果
        print(result)
    finally:
        cursor.close()
        conn.commit()
        conn.close()

def database_operator_read(name):
    conn   = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('select * from ' + name + 'table')

    result = cursor.fetchall()
    # 打印查询结果
    print("read table")
    print(result)

    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("sqlite3 database test")
    init_log()

    try:
        #init_sqlite_database()
        #project_test()
        #read_table()
        database_operator_init('veer','world')
        database_operator_read('veer')
    except Exception as e:
        logging.info(e) 
        print(e)
