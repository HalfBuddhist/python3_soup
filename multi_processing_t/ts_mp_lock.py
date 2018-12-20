#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/27
"""测试多进程下锁的使用

结论：
1. 不使用锁会乱序，多进程变量如果在多个进程中被写的话，结果难以预知。
2. 进程间不直接共享变量，可以认为传入的是一个深拷贝，不会动态随其它的进程的读写而变化。
"""

import multiprocessing as mp
import time

class V(object):
    pass

l = mp.Lock()  # 定义一个进程锁
# v = V()
# v.value = 0

def job(v, num):
    l.acquire()  # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        print(v.value)
    l.release()  # 释放


def multicore():
    v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job, args=(v, 1))  # 需要将lock传入
    p2 = mp.Process(target=job, args=(v, 3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
