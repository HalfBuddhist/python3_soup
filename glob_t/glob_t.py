# Copyright (c) 2018 Ainnovation.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2020/4/15
"""
"""

import glob
import os

# support exact match, wildcard in the midle path or file name.
for e in glob.glob("/Users/administrator/workspace/pycharm/*/*.py"):
    print(e, type(e))
