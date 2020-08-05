# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/25
"""return 语句在生成器中用于中止当前生成器，如果调用next、send执行到他就会报stopIteration
其后的参数（python>3.3版本支持）作为抛出的 StopIteration 异常的参数。
"""


def f1():
    for i in range(10):
        print(i)
        i += 1
        yield i
        return i+1

f = f1()
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)