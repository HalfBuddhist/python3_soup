# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/4/16
"""测试 kazoo 多进程与多线程中的读取

结论：
kazooClient不支持在多进程你共享客户端，
强制共享会卡在 zookeeper 操作中，如 get_childredn('/')

Client 支持在多线程中的共享。
"""

import multiprocessing
import threading

from kazoo.client import KazooClient

zk = KazooClient(hosts="ubuntu-qz:2181")
zk.start()


def getChildren():
    print('start')
    print(zk.get_children('/'))


if __name__ == '__main__':
    # one process
    getChildren()

    # multi process
    # process = multiprocessing.Process(target=getChildren)
    # process.start()
    # print("waiting for finished.")
    # process.join()

    # multi threading
    thread = threading.Thread(target=getChildren)
    thread.start()
