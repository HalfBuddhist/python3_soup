# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/6/24
"""测试 Pulsar MQ 的一些边界：

1. consumer 的 unsubscribe 相当于是 close, 同时使用会报错,
    于 client.close 后面使用会报错，producer 也是。
2.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import datetime
import sys
from _pulsar import ConsumerType
from threading import Timer

import pulsar

def main(argv):
    host = '192.168.50.233'
    port = 6650
    topic = 'test_channel'
    client = pulsar.Client('pulsar://{}:{}'.format(host, port))
    producer = client.create_producer(topic)
    for i in range(10):
        producer.send(("hello-%s" % i).encode("utf-8"))
    print("Finished produce message.")
    client.close()


if __name__ == '__main__':
    main(sys.argv)
