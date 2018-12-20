#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/27
"""获取本机IP 1

但是注意这里获取的IP是内网IP
"""

import socket

#获取本机电脑名
myname = socket.getfqdn(socket.gethostname())
#获取本机ip
myaddr = socket.gethostbyname(myname)
print(myname)
print(myaddr)
