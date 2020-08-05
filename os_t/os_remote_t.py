# Copyright (c) 2018 Ainnovation.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2020/4/15
"""OS func soup

全部原生不支持通配符
"""

import glob
import os
import shutil

# delete one file
# os.remove('/Users/administrator/workspace/pycharm/python3_soup/os_t/a.txt')

# delete empty directory
# os.removedirs('/Users/administrator/workspace/pycharm/python3_soup/os_t/a*')
# os.rmdir('/Users/administrator/workspace/pycharm/python3_soup/os_t/a')

# delete non-empty directory, can't delete single file
shutil.rmtree('/Users/administrator/workspace/pycharm/python3_soup/os_t/aa')
