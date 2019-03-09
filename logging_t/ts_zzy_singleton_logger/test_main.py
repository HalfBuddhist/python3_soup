# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: Zhiya Zang <zangzhiya@chuangxin.com>
# Date:   2019-01-18
"""zzy logger test.

分析：应该是可以的，毕竟是进程开始前就设定过的，拷贝已有内存而并没有共享修改。

单子其实并不能解决问题，因为，这个单子不能多进程，
单子只是在单进程内确保唯一，多进程时，会都从父进程 copy 过来，
在只读的条件下，父子进程看起来是共用一个。

记录一下，这里 LoggerHelper 初始化一次因为创建新进程前已经 setup 过，
所以创建进程时候复制的 LoggerHelper 单例已经初始化过了，
但是实际上他们在不同进程中是不同的对象，并没有真正的共享。

试了一下发现竟然没问题, 分别用 multiprocessing 和 concurrent 模拟了多进程，
发现 LoggerHelper 只初始化了一次。

记录一下，创建新进程时候，系统会创建虚拟地址空间，
将 setup 过的 LoggerHelper 单例复制到新的进程中，
但是在没有 write 动作时并不会真正复制物理空间中的对象（copy-on-wirte），
所以实际上不同进程中的 LoggerHelper 还是指向同一个对象。
因为 LoggerHelper 已经 setup 过，所以复制（虚拟的复制）到子进程之后，就不需要重新初始化了。
"""

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

import runtime_path
from utils.logger import LoggerHelper


def log():
    logger = LoggerHelper().get_logger('sub_logger')
    logger.info('sub_logger info')
    logger.warn('sub_logger warn')
    logger.error('sub_logger error')


def main():
    LoggerHelper().setup('helper', '/home/zzy/Desktop/test/log')
    outer_logger = LoggerHelper().get_logger('main_logger')
    outer_logger.info('main_logger info')
    outer_logger.warn('main_logger warn')
    outer_logger.error('main_logger error')

    f = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        f.append(executor.submit(log))
        f.append(executor.submit(log))
        f.append(executor.submit(log))

    for item in f:
        item.result()

    proc = Process(target=log)
    proc.start()
    proc.join()


if __name__ == '__main__':
    main()
