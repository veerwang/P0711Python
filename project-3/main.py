#! /usr/bin/python
#coding=utf-8

if __name__ == '__main__':
    strmyage = input('Enter your Age:')
    myage = int(strmyage)                   #注意此处的转换
    if myage > 18: 
        print('you are a man!')
    else:
        print('you are a boy!')
