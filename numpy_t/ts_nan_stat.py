#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/1/17
"""python numpy 判断ndarray 中是否有 nan
同理也可判断 inf
"""

import numpy as np

data = np.array([1, 2, 3, np.nan, 4, np.nan])
# 获得一个bool数组
print(np.isnan(data))

# array([False, False, False,  True, False,  True], dtype=bool)

# 这样可以获得nan的数量
print(np.isnan(data).sum())
# 2