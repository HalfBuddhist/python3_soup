#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/1/28
"""测试 python 中 logger 的继承链设置逻辑
换句句话说我们可以通过 xxx.xxx 的形式获取任何一级的 logger，但是这些中间层的 logger
并不一定是存在的，如果不存在，则不会自动创建，而是会将 parent 设置成root, 如果存在，
则按点分隔的具体来形成parent。

如果我们在 base 中也创建⼀一个 logger，logger.getLogger('base') ，
这时候，base logger 也 继承⾃自 root logger，
但是 db logger 的继承顺序则被修改成了了继承⾃自 base logger。
"""

import logging

root = logging.getLogger()
base_db = logging.getLogger("base.db")
print(base_db.parent)
base = logging.getLogger("base")
print(base_db.parent)
