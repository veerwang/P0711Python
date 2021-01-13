#! /usr/bin/python
#coding=utf-8

"""
 描述:		工程测试		 
 创建人:	kevin.wang
 创建日期:	2021年01月13日 
 版本:		1.0.0     
 """

import os
import curses
import time

if __name__ == '__main__':
    print("curses detect")
    stdscr = curses.initscr()
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.addstr(2,2,"程序电子",curses.color_pair(1))
    stdscr.refresh()
    time.sleep(2)
    curses.endwin()
