# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/16
# coding=utf-8
"""
"""

import numpy as np


def k(xs, ys, sigma=1, l=1):
    """Sqared Exponential kernel as above but designed to return the whole
    covariance matrix - i.e. the pairwise covariance of the vectors xs & ys.
    Also with two parameters which are discussed at the end.
    """
    # Pairwise difference matrix.
    xe = np.expand_dims(xs, 1)
    ye = np.expand_dims(ys, 0)
    dx = xe - ye
    return (sigma ** 2) * np.exp(-((dx / l) ** 2) / 2)


N = 100
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
d = k(x, y)

print(d)
