# Copyright (c) 2018 Ainnovation.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/8/27
"""
"""

# import b
#
# b.a_hello()
# b.b_hello()
# print(b.a_var)
# print(b.b_var)

import importlib
bb = importlib.import_module('dynamic_import.b')

bb.a_hello()
bb.b_hello()
print(bb.a_var)
print(bb.b_var)

