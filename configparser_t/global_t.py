# Copyright (c) 2018 Ainnovation.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2020/6/30
"""Test ConfigParser
"""

import configparser

config = configparser.ConfigParser()

# for demo.ini
res = config.read('./global.ini')
print(res)

secs = config.sections()
print(secs)

value = config['all']
print(value)
