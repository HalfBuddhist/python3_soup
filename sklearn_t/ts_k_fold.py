# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/26
"""
"""

from sklearn.model_selection import KFold
import pandas as pd

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
s = pd.Series(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

fold = KFold(4)

gen1 = fold.split(a)
print(type(gen1), id(gen1))

gen2 = fold.split(s)
print(type(gen2), id(gen2))

for t, v in gen1:
    print(t, v)
    # print(type(t), type(v))  # type is ndarray.


print('#' * 20)


for t, v in gen2:
    print(t, v)
    print(s.iloc[t])
    print(s.iloc[v])
# print(s)


c = ['a']
fold = KFold(1)
gen_c = fold.split(c)
for t, v in gen_c:
    print(t, v)
