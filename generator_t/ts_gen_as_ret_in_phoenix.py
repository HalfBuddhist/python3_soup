# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/2
# coding=utf-8
"""测试生成器在phoenix中做为返回值的情况。

最好将yield单独封装一下，否则会误以为生成生成器本身的函数是生成器，就像get_generator_4_hp
函数中的single_gen中一样对其进行封装。
"""

from ConfigSpace import CategoricalHyperparameter, UniformFloatHyperparameter, UniformIntegerHyperparameter

SAMPLES_ON_INTEGER_FEATURE = 5  # none negtive value.
SAMPLES_ON_FLOAT_FEATURE = 5    # none negtive value.


def get_generator_4_hp3(hyper_param):
    """Get generator for the hyperparameter
    TODO(liuqw) resolve more hyperparameters' type.
    :param hyper_param:
    :return: Generator to iterate on the hypermeter.
    """
    def single_gen(value):
        yield value

    if isinstance(hyper_param, CategoricalHyperparameter):
        return (x for x in hyper_param.choices)
    elif isinstance(hyper_param, UniformFloatHyperparameter):
        return single_gen(hyper_param.default)
    else:
        raise Exception("Not supported hyperparameter "
                                            "type: %s", type(hyper_param))


def get_generator_4_hp2(hyper_param):
    if isinstance(hyper_param, CategoricalHyperparameter):
        return (x for x in hyper_param.choices)


def get_generator_4_hp(hyper_param):
    """Get generator for the hyperparameter
    TODO(liuqw) resolve more hyperparameters' type.
    :param hyper_param:
    :return: Generator to iterate on the hypermeter.
    """
    def single_gen(value):
        yield value

    if isinstance(hyper_param, CategoricalHyperparameter):
        return (x for x in hyper_param.choices)
    elif isinstance(hyper_param, UniformFloatHyperparameter):
        if SAMPLES_ON_FLOAT_FEATURE < 0:
            raise Exception("Require none negtive para.")
        elif SAMPLES_ON_FLOAT_FEATURE in (0, 1):
            return single_gen(hyper_param.default)
        else:
            step = ((hyper_param.upper - hyper_param.lower) /
                    (SAMPLES_ON_FLOAT_FEATURE - 1))
            return ((hyper_param.lower + i * step) for i in
                    range(SAMPLES_ON_FLOAT_FEATURE))
    elif isinstance(hyper_param, UniformIntegerHyperparameter):
        if SAMPLES_ON_INTEGER_FEATURE < 0:
            raise Exception("Require none negtive para.")
        elif SAMPLES_ON_INTEGER_FEATURE in (0, 1):
            return single_gen(hyper_param.default)
        elif (SAMPLES_ON_INTEGER_FEATURE >
              (hyper_param.upper + 1 - hyper_param.lower)):
            return (x for x in range(hyper_param.lower, hyper_param.upper + 1))
        else:
            step = ((hyper_param.upper - hyper_param.lower) //
                    (SAMPLES_ON_INTEGER_FEATURE - 1))
            return (x for x in range(hyper_param.lower,
                                     hyper_param.upper + 1, step))
    else:
        raise Exception("Not supported hyperparameter "
                                            "type: %s", type(hyper_param))


f6 = CategoricalHyperparameter("param", ["a", "b", "c", "d", "e"], default="b")

gen = get_generator_4_hp(f6)

# print(type(get_generator_4_hp(f6)), type(get_generator_4_hp2(f6)))

for x in gen:
    print(x)

# value = next(gen)

# print(value)