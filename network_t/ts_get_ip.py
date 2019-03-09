#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/9/27
"""获取本机IP 1

但是注意这里获取的IP是内网IP, linux 下可用，

mac Mojava 下 gethostbyname，默认会报 gaierror 异常的错误，改一下主机名（computer name）
就可以了，不要用默认的电脑名, 这样还是会出错，使用gethostbyname，里面参数填hostname，
而不是 domain name 时则不会出错。
"""

import socket

#获取本机电脑名
hostname = socket.gethostname()
print(hostname, type(hostname))
myname = socket.getfqdn(hostname)
print(myname, type(myname))

#获取本机ip
# myaddr = socket.gethostbyname(myname)
# print(myaddr, type(myaddr))
myaddr = socket.gethostbyname(hostname)
print(myaddr, type(myaddr))

print(socket.gethostbyname('localhost'))
print(socket.gethostbyname(''))
