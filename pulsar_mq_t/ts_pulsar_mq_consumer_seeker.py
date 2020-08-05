# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/6/24
"""测试 Pulsar MQ 的一些边界：

1. 在使用 seek 进行队列cursor定位时，请将receiver_queue_size设为1，
    如果设为较大，broker 会认为你在取了很多消息还没有处理完，同时重置在 broker中的头指针
    因此会断开链接，以至于报NoeConnected 的异常。

    设置请将receiver_queue_size设为1为1时会执行两次，是因为预取了一个，相当于取了两个。
    在万国情境中，由于一次并不是产生很多个，所以 receive 函数只取回了一个，
    执行完成后，虽然产生了很多，由于置为了 latest, 且由于上次没有预取，所以 receive 函数
    会再去 broker 中去取，会卡在那里，又会只取到一个，预取失败，如此循环，相当于是将
    receiver_queue_size设为了0。

    莫名的将receiver_queue_size设为了0，会报InvalidConfiguration异常。
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import datetime
import sys
from _pulsar import ConsumerType
from threading import Timer
from time import sleep

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

    for i in range(11):
        consumer.seek(pulsar.MessageId.latest)
        msg_raw = consumer.receive()
        print(msg_raw.data().decode("utf-8"))
        consumer.acknowledge(msg_raw.message_id())
        sleep(5)

    # consumer.unsubscribe()
    consumer.close()
    client.close()


if __name__ == '__main__':
    main(sys.argv)
