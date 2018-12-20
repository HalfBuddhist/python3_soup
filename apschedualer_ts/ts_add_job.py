#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/10/26
"""
"""

from apscheduler.schedulers.blocking import BlockingScheduler


class TT(object):
    def __init__(self):
        self._sched = BlockingScheduler()

    def hello(self):
        print('hello')

    def start(self):
        self._sched.add_job(self.hello, 'cron', hour=17, minute=25)
        # self._sched.add_job(self.hello, 'interval', seconds=1)
        self._sched.start()


if __name__ == '__main__':
    tt = TT()
    tt.start()
