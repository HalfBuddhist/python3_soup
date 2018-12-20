#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/21
"""测试logger没有config的情况下，获取名字相同的logger是否会是相同的。

结论：是相同的，既然对象是相同的，那么其属性也是相同的，所以其handler与formatter也是相同的。
    父logger与子logger是不同的对象，想想也知道，如果是同一个propagate参数就没有意义了。
"""

import logging

a = logging.getLogger("b")

from ts_logger_same_name_2 import c

print(a == c)
print(a is c)
print(id(a), id(c))

d = logging.getLogger("b.d")

print(a == d)
print(a is d)
print(id(a), id(d))