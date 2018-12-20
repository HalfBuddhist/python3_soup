#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/8
"""send mail general procedure.
"""

import smtplib
from email.mime.text import MIMEText

# 设置服务器所需信息
# 163邮箱服务器地址
mail_host = 'smtp.163.com'
# mail_host = 'outlook.office365.com'
# mail_host = 'smtp.office365.com'
# 163用户名
# mail_user = 'liuqingwei-forward'
mail_user = 'mli_phoenix'
# mail_user = 'liuqingwei@chuangxin.com'
# 密码(部分邮箱为授权码)
mail_pass = 'TSNA7CDYJT8PVZC9'
# 邮件发送方邮箱地址
sender = 'mli_phoenix@163.com'
# sender = 'liuqingwei@chuangxin.com'
# 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['liuqingwei2019@gmail.com', 'liuqingwei@chuangxin.com']

# 设置email信息
# 邮件内容设置
message = MIMEText('content', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = 'title'
# 发送方信息
message['From'] = sender
# 接受方信息
message['To'] = receivers[0]

# 登录并发送邮件, 普通邮件
try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    # smtpObj.connect(mail_host, 25)
    # smtpObj.connect(mail_host, 587)
    # smtpObj = smtplib.SMTP_SSL(mail_host, 25)  # 发件人邮箱中的SMTP服务器
    # smtpObj.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
    # smtpObj.starttls()
    # smtpObj.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
    # 登录到服务器
    smtpObj.login(mail_user, mail_pass)
    # 发送
    smtpObj.sendmail(sender, receivers, message.as_string())
    # 退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    # 打印错误
    print('error: ', e)
