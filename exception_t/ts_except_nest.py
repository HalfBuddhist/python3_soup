#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/17
"""Exception可以嵌套，内部不抛出，外部就捕获不到。
"""


def a():
    print("hello")
    raise Exception


try:
    for x in range(10):
        try:
            a()
        except Exception as e:
            print("Nest except: {}".format(str(e)))
            break
except Exception as e:
    print("Outer except:{}".format(str(e)))
