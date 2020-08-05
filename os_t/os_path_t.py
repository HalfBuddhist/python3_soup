# Copyright (c) 2018 Ainnovation.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2020/4/15
"""os path function soup
"""
import os

# 得到所在目录的名字
print(os.path.dirname('/a/b/b'))
print(os.path.dirname(''))

# 得到绝对路径
print(os.path.abspath('/a/b/b'))
# 得到绝对路径，如果为空，则为当前working directory
print(os.path.abspath(''))

# 得到路径数据[上层目录名, 文件名]
print(os.path.split('/a/b/*.txt'))
(a, b) = os.path.split('/a/b/*.txt')
print(a, b)
