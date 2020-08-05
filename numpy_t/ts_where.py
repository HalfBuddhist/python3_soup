# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/27
"""
"""
import pandas as pd
import numpy as np

s = pd.Series({6: 'a', 44: 'b', 5: 'c', 33: 'w'})
print(s)

res = np.where(s > 'a')
print(res, type(res))
print(res[0], type(res[0]))

print(s[s > 'a'])
