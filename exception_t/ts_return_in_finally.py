#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/20
"""测试finally语句中如果发return如何进行处理。

finally中如果return，后面的语句就不会执行了，而且会覆盖以前抛出的结果。
另外，try与except中的return 与 raise 都会执行 finally 中的语句。
"""


def f1():
    try:
        raise Exception
        # return 1
    except Exception as e:
        print(str(e))
        return 3
    finally:
        print("in finally")
        # return 2
        print("do me or not?")


a = f1()
print(a)
