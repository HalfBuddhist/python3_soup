# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/6/27
# coding=utf-8
"""测试生成器表达式做为参数的形式

可以将表达式中的小括号删除。
"""


def func(p_iterator):
    for item in p_iterator:
        print(item)


func([x for x in range(10) if x % 2 == 0])
