#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/27
"""测试多进程下共享数据：

1，进程本身不共享数据（区别于线程，线程是可以共享全局变量的），共享的数据可以用 Value 与 Array 来保存。
2，或者通过第三方进程的方法 Manager 来保存数据 (如 dict, list 等数据类型)。
"""

import multiprocessing as mp
import time

class V(object):
    pass

l = mp.Lock()  # 定义一个进程锁
# v = V()
# v.value = 0

# data_mg = mp.Manager()
# v = data_mg.dict()
v = dict()

def job(num):
    l.acquire()  # 锁住
    for x in range(5):
        time.sleep(0.1)
        v[x] = x + num
        # print(v.value)
    l.release()  # 释放
    print(str(v))


def multicore():
    # v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job, args=(1,))  # 需要将lock传入
    p2 = mp.Process(target=job, args=(3,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(str(v))


if __name__ == '__main__':
    multicore()
