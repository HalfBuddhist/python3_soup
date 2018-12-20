#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/21
"""测试 pickle 模块的基本用法
"""

import pickle

# dumps功能
data = ['aa', 'bb', 'cc']
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)

# loads功能
# loads  将pickle数据转换为python的数据结构
mes = pickle.loads(p_str)
print(mes, type(mes))

# dump 功能
# dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('tmp.pk', 'wb') as f:
    pickle.dump(data, f)

# load功能
# load 从数据文件中读取数据，并转换为python的数据结构
with open('tmp.pk', 'rb') as f:
    data = pickle.load(f)
    print(data, type(data))
