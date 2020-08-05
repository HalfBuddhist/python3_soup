#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/20
"""测试except语句中如果raise, finally中的语句是否会执行

结论： 会执行
"""


def f1():
    try:
        raise Exception("self throwed exception")
        # return 1
    except Exception as e:
        print(str(e))
        raise e
    finally:
        print("in finally")
        # return 2
        print("do me or not?")


a = f1()
print(a)
