# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/6/29
# coding=utf-8
"""The step in range func could not be 0!
"""

for t in range(0, 10, 1):
    print(t)

x = range(1, 10)
print(type(x))