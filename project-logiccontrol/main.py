#! /usr/bin/env python3
#coding=utf-8

def main():
    x = 5
    while(x):
        print("hello world")
        x = x - 1
        if x == 2:
            break
        elif x == 3:
            print("x=3")
        else:
            print("loop normal end")

    for i in range(5):
        print(str(i))

if __name__=="__main__":
    main()
