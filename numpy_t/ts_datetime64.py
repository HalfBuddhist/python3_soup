# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/27
"""
"""

import numpy as np

a = np.array(['2007-07-13', '2006-01-13', '2010-08-13'], dtype='datetime64')
print(repr(a))
print(a[0], type(a[0]))

d = np.datetime64('2009-01-01') - np.datetime64('2008-01-01')
print(d, repr(d))
print(d*0.5)