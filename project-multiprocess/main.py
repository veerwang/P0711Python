#! /usr/bin/python
#coding=utf-8

#
# 描述:		工程测试		 
# 创建人: 	kevin.wang
# 创建日期:     2019年10月29日 
# 版本:		1.0.0     
# 参考网页
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064

from multiprocessing import Process,Queue,Pipe
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
    # 如果进程池进行了close,那么就不能再创建多进程了。
    p.close()
    # 等待其他进程的结束
    p.join()
    print('All subprocesses done.')

########################################
# 多进程，信息传递
#

# 写数据进程执行的代码:
def process_write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

    # 通过queue进行通讯可以传输不同的类型的数据，只是数据的传输是有一定的顺序的
    command_list = ['kevin','wangwei','veer']
    q.put(command_list)

# 读数据进程执行的代码:
def process_read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        # 阻塞的
        value = q.get(True)
        print('Get %s from queue.' % value)

def communication_process():
    q = Queue()
    pw = Process(target=process_write, args=(q,))
    pr = Process(target=process_read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

# 通过pipe进行通讯
def after(conn):
    for i in range(10):
        print("接收到数据:", conn.recv())
        time.sleep(1)
def before(conn):
    for i in range(10):
        data = [42, None, 34, 'hello']
        conn.send(data)
        print("正在发送数据：%s" % (data))
        time.sleep(1)

def apipe_process():
    # after_conn与before_conn是一个管道的两个端
    after_conn,before_conn = Pipe()

    p1 = Process(target=after, args=(after_conn,))
    p1.start()

    p2 = Process(target=before, args=(before_conn,))
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    apipe_process()
    print("<========>")
    single_process()
    print("<========>")
    multi_process()
    print("<========>")
    communication_process()
