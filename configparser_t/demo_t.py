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
res = config.read('./demo.ini')
print(res)

secs = config.sections()
print(secs)

value = config['Server']['port']
print(value)

value = config['Server']['name']
print(value)
