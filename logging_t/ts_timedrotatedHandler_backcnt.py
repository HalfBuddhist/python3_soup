#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/10/23
"""
"""

import logging
from logging.handlers import TimedRotatingFileHandler

log_handler = TimedRotatingFileHandler("ts_timed_rotated/ts_timed_rotated.log",
                                       encoding="utf-8",
                                       backupCount=3,
                                       when='midnight')

_formatter = logging.Formatter(
        "[%(asctime)s] [%(name)s] [%(filename)s(%(lineno)d)] "
        "[%(levelname)s] %(message)s",
        "%Y-%m-%d %H:%M:%S")

log_handler.setLevel(logging.DEBUG)
log_handler.suffix = "%Y-%m-%d"
log_handler.setFormatter(_formatter)

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

for i in range(3):
    logger.info("log %d" % i)
