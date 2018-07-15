#! /usr/bin/python
#coding=utf-8


def main():
    x = 5
    while(x):
        print("hello world")
        x = x - 1
        if x == 2:
            break
    else:
        print("loop normal end")


if __name__=="__main__":
    main()
