# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/15
"""ensure the x to be an column, else raise and exception.
"""
import numpy as np

n = np.arange(0, 30, 2)
# n = n.reshape(3, 5)
print(n)

from sklearn.utils.validation import column_or_1d

x = column_or_1d(n)
print(type(x))
