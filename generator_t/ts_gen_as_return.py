# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/2
# coding=utf-8
"""测试生成器做为返回值的情况。

可以做为返回值，正常运行。
"""

tt = "hello"

def func_ret_gen():
    return (yield 'hello')


def func_ret_gen2():
    return (x for x in range(0, 10))


def func_ret_gen3(p_str):
    return (x for x in p_str)

# a = func_ret_gen2()
a = func_ret_gen3(tt)

print(type(a))

for i in a:
    print(i)
