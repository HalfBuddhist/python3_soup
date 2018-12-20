#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/8
"""以 163, smtp, 465 port 邮箱为发送邮箱发送邮件
"""

import smtplib
from email.mime.text import MIMEText

mailserver = smtplib.SMTP_SSL('smtp.163.com', 465)
# mailserver.ehlo()
# mailserver.starttls()
# mailserver.ehlo()
mailserver.login('mli_phoenix', 'TSNA7CDYJT8PVZC9')

# 邮件内容设置
message = MIMEText('content', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = 'title'
# 发送方信息
message['From'] = 'mli_phoenix@163.com'
# 接受方信息
message['To'] = "qingwei.liu@foxmail.com"

mailserver.sendmail('mli_phoenix@163.com', 'qingwei.liu@foxmail.com',
                    message.as_string())
# identified as a spam in 163 for the body, code: 554 DT:SPM
# mailserver.sendmail('liuqingwei@chuangxin.com', 'qingwei.liu@foxmail.com',
#                     'python mail')
mailserver.quit()
