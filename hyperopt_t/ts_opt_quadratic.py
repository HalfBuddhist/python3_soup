# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/5
# coding=utf-8
"""test the opt by optimizing a quadratic func.
"""

from hyperopt import hp, fmin, tpe, rand, space_eval

space = [hp.uniform('x', 0, 1), hp.normal('y', 0, 1)]

def f(args):
    x, y = args
    return x**2 + y**2

best = fmin(f, space, algo=rand.suggest, max_evals=100)

print("random: {}".format(best))


