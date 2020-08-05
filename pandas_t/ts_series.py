# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/26
"""
"""

import pandas as pd
from numpy import *

list2 = [10, 20, 30, 40, 50]
indexlist = ['a', 'b', 'c', 'd', 'e']

series = pd.Series(list2, index=indexlist)
print('series的值：', series.values)
print('series的标签：', series.index)
# 即可以像数组一样检索，也可以像字典一样检索
print('b:', series['b'])
print('the third:', series[3])
# series支持字典的一些方法
print(list(series.iteritems()))
# 一些运算
print('取标签大于c的项：', '\n', series[series.index > 'c'])
print('取值大于20的项：', '\n', series[series.values > 20])
print('将每一项中的数×2', '\n', series * 2)
dict = {'nihao': 1, 'wode': 2, 'bushi': 3}
series2 = pd.Series(dict)
print('将字典转化为series：', '\n', series2)


dict_list = [{'nihao': 1, 'wode': 2, 'bushi': 3},
        {'nihao': 1, 'wode': 2, 'bushi': 3},
        {'nihao': 1, 'wode': 2, 'bushi': 3}]
series3 = pd.Series(dict_list)
print('将字典转化为series：', '\n', series3)