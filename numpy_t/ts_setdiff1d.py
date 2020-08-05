# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/25
"""测试 setdiff1d(arr1, arr2)
返回在 arr1 却不在 arr2 中元素列表。
"""
import numpy as np

x = np.array([1, 2, 3, 4, 1, 2, 6])
uniq_clas = np.array([1, 2, 3, 4])
classes = np.unique(x)
print("unique class: ", classes)

unseen_class = np.setdiff1d(classes, uniq_clas)
print("unseen_class: ", unseen_class)
