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
    subscriber = 'sub'
    client = pulsar.Client('pulsar://{}:{}'.format(host, port))
    consumer = client.subscribe(topic, subscriber,
                                consumer_type=ConsumerType.Shared,
                                receiver_queue_size=1)
    # consumer.redeliver_unacknowledged_messages()
    for i in range(1):
        msg_raw = consumer.receive()
        print(msg_raw.data().decode("utf-8"))
        consumer.acknowledge(msg_raw.message_id())

    # consumer.unsubscribe()
    consumer.close()
    client.close()


if __name__ == '__main__':
    main(sys.argv)
