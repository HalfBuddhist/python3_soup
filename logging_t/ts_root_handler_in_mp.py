#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/1/29
"""多线程下的 logger 竟然是相同的，无缝共享。
应该是 copy on write 机制 。
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from multiprocessing import Process


root_1 = logging.getLogger()
print(id(root_1))

def func():
    root = logging.getLogger()
    root.setLevel(logging.WARN)
    root.addHandler(
        TimedRotatingFileHandler("/Users/administrator/Downloads/t.log",
                                 backupCount=180, encoding="utf-8",
                                 when='midnight'))
    print(id(root))
    print(root == root_1)


pp = Process(target=func())
pp.start()
pp.join()
print("finished.")