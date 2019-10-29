#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月29日 
# 版本:		1.0.0     
# 参考网页
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064

from multiprocessing import Process
from multiprocessing import Pool 
import os,time,random

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def single_process():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

########################################
# 多进程
#
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def multi_process():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

if __name__ == '__main__':
    single_process()
    print("<========>")
    multi_process()
