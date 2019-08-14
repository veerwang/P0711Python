#! /usr/bin/python
#coding=utf-8

def create_file():
    filehandle = open("./data/README",'w')
    filehandle.write('the file\n')
    filehandle.close()

if __name__ == '__main__':
    print('hello the world')
    create_file()
