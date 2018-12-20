#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/8
"""以 outlook 邮箱为发送邮箱发送邮件
"""

import smtplib
from email.mime.text import MIMEText

mailserver = smtplib.SMTP('smtp.office365.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('liuqingwei@chuangxin.com', 'cx_252019')

# 邮件内容设置
message = MIMEText('content', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = 'title'
# 发送方信息
message['From'] = 'liuqingwei@chuangxin.com'
# 接受方信息
message['To'] = "qingwei.liu@foxmail.com"

mailserver.sendmail('liuqingwei@chuangxin.com', 'qingwei.liu@foxmail.com',
                    message.as_string())
# identified as a spam in gmail for the body
# mailserver.sendmail('liuqingwei@chuangxin.com', 'qingwei.liu@foxmail.com',
#                     'python mail')
mailserver.quit()
