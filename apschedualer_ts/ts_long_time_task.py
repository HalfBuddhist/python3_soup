# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/22
"""测试长时间任务超过间隔时，任务的循环执行情况。
由schedualer.add_job函数中的 max_instances来判定，默认为1.
"""

from time import sleep

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import random

class TT(object):

    def __init__(self):
        self._sched = BlockingScheduler()
        # self._sched = AsyncIOScheduler()
        # self._sched = BackgroundScheduler()

    def hello(self):
        tag = random.randint(0, 100)
        print('hello, %s' % tag)
        sleep(5)
        print('finish, %s' % tag)

    def start(self):
        # self._sched.add_job(self.hello, 'cron', hour=17, minute=46)
        self._sched.add_job(self.hello, 'interval', seconds=2, max_instances=2)
        self._sched.start()


if __name__ == '__main__':
    tt = TT()
    tt.start()
