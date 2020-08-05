#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/10/26
"""Test the apschedualer module function.
"""
from time import sleep

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


class TT(object):

    def __init__(self):
        # self._sched = BlockingScheduler()
        self._sched = AsyncIOScheduler()
        self._sched = BackgroundScheduler()

    def hello(self):
        print('hello')

    def start(self):
        # self._sched.add_job(self.hello, 'cron', hour=17, minute=46)
        self._sched.add_job(self.hello, 'interval', seconds=1)
        self._sched.start()
        print('hello world.')
        sleep(10)
        self._sched.remove_all_jobs()
        print('remove jobs')
        sleep(10)
        self._sched.add_job(self.hello, 'interval', seconds=1)
        print('add new jobs')
        sleep(10)


if __name__ == '__main__':
    tt = TT()
    tt.start()
