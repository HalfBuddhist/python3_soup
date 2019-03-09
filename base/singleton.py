# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: Zhiya Zang <zangzhiya@chuangxin.com>
# Date:   09/01/2018


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
