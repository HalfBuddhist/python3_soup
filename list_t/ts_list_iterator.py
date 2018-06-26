# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/6/26
# coding=utf-8

"""使用for循环来遍历访问一个迭代器时，在遍历结束时并没有抛出StopIteration,
感觉应该是python解释器优化的结果。
但在生成器时好像是会抛出的。
"""

a = list([1, 2, 3, 4])

for x in a:
    print(x)


class TestIterator(object):

    def __init__(self, arr):
        self._arr = arr
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._arr):
            raise StopIteration
        else:
            self._index += 1
            return self._arr[self._index - 1]


a = TestIterator([1, 2, 3, 4])

for x in a:
    print(x)
