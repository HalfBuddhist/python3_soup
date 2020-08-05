# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/6/24
"""测试 Pulsar MQ 的一些边界的行为：

1. consumer 的 unsubscribe 相当于是 close, 同时使用会报错,
    于 client.close 后面使用会报错，producer 也是。
2. 如果开两个shared client 其中一个注销预订，另一个会怎么样？
    注销会报错，另一个会正常订阅，但使用上面的 consumer 的close 方法就不会报错。
3. consumer 的 close 方法会取消注册吗？
    需要知道查看注册者有哪些的命令，
    ./pulsar-admin topics subscriptions persistent://tenant/namespace/topic
    不会取消注册，只是关闭了 consumer, 没有取消注册。
4. 推送到一个没有subscripter 的 topic 下，消息会怎么样？
   保存一定时间后删除, 只有有订阅者时才不会删除。
5.
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
    topic = 'test_channel1'
    subscriber = 'sub'
    client = pulsar.Client('pulsar://{}:{}'.format(host, port))
    producer = client.create_producer(topic)
    for i in range(10):
        producer.send(("hello-%s" % i).encode("utf-8"))
    print("Finished produce message.")

    consumer = client.subscribe(topic, subscriber,
                                consumer_type=ConsumerType.Shared)
    for i in range(100):
        msg_raw = consumer.receive()
        print(msg_raw.data().decode("utf-8"))
        consumer.acknowledge(msg_raw.message_id())

    consumer.unsubscribe()
    # consumer.close()
    client.close()
    # consumer.unsubscribe()


if __name__ == '__main__':
    main(sys.argv)
