# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/6/26
# coding=utf-8

"""两种异常的抛出方式的区别

一种是使用默认的参数，一种是添加了一个字符串做为异常的描述型参数。
"""

def func_raise():
    raise Exception


def func_raise2():
    raise Exception("hello world.")


try:
    func_raise2()
except Exception as e:
    print("Exception happens!")
    print(str(e))
    print(e.__doc__)
    print(e.__repr__())


