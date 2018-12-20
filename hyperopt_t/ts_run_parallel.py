# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/9
# coding=utf-8
"""test the hyperopt in parallel
"""

from hyperopt import hp, fmin, tpe, rand, space_eval, Trials
from hyperopt.mongoexp import MongoTrials
import time
import math
from hyperopt import fmin, tpe, hp, Trials


def fn_obj(args):
    # time.sleep(3)
    return math.sin(args)


def main():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # trials = Trials()
    trials = MongoTrials('mongo://localhost:27017/ts_hyperopt/jobs',
                         exp_key='exp1')
    best = fmin(fn_obj, hp.uniform('x', -2, 2), trials=trials,
                algo=tpe.suggest, max_evals=100)

    # for t in trials:
    #     print(t)

    print(best)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == '__main__':
    main()
