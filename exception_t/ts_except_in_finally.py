#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/20
"""测试finally语句中如果发生的异常应该如何进行处理。

Finally中如果抛出异常，后面的语句就不会执行了，
而且会覆盖以前抛出的结果(include return and except)。
"""


def f1():
    try:
        raise Exception("internal except.")
    except Exception as e:
        print(str(e))
        raise Exception("middle except.")
    finally:
        print("in finally")
        raise Exception("except in finally.")
        print("do me or not?")


try:
    f1()
except Exception as e:
    print(str(e))
