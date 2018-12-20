#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/27
"""测试线程是否可以共享变量来传递内容。

结论：
1，可以，如果两者都需要写操作的话，最好加上锁，否则可以不加锁。
"""

import threading
import time

i = 0


def func_add(thread_num):
    global i
    for _ in range(5):
        i += 1
        print(thread_num, i)
        # print(thread_num, "hello world.")
        time.sleep(1)
    print(thread_num, "Final: %s" % i)


# method1: start by threading.
thread1 = threading.Thread(target=func_add, args=(1, ))
thread2 = threading.Thread(target=func_add, args=(2, ))
print("start thread1")
thread1.start()
print("start thread2")
thread2.start()
print("Join")
thread1.join()
thread2.join()
print("main", i)
pass
