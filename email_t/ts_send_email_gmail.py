# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/2
# coding=utf-8
"""free test
if (/(?:^|\.)googleadservices\.com$/.test(host)) return "+SS";
"""

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


gmail_user = 'liuqingwei2019@gmail.com'   # Your Gmail or Google Apps username
gmail_password = 'htvviqabdjjrxsds'  # Your Gmail or Google Apps password

sent_from = gmail_user # You can change this to another alias in your Gmail account
send_to = ['qingwei.liu@foxmail.com', ]   # TO this list of email addresses
# send_cc = ['great-cc-example@somewhere.com']   #  CC to this list of email addresses
# send_bcc = ['good-bcc-examplen@someplace.com']  # BCC to this list of email addresses
subject = "Your Subject"  # The subject of your message

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] =  subject
msg['From'] = sent_from
msg['To'] = ", ".join(send_to)
# msg['cc'] = ", ".join(send_cc)

# Plaintext version of the email
text = "Plain text if HTML is not supported by the receiving email client"

# HTML version of the email
html = f"""\
&lt;html&gt;
  &lt;head&gt;
  &lt;/head&gt;
  &lt;body&gt;
    Put your HTML code here!
  &lt;/body&gt;
&lt;/html&gt;
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # We are specifying TLS here
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, send_to, msg.as_string())
    # server.sendmail(sent_from, send_to + send_cc + send_bcc, msg.as_string())
    server.close()
    print( 'Email(s) Sent')
except:
    print('Error Sending Email(s)')
