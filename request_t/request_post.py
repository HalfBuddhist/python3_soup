# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/4/18
"""requests 发送数据编码情况：

1. 直接使用 unicode即可，库会自动的将其先用utf-8编码，
   再用url-encode 来编码（如果使用默认值参数的情况下）。
"""

import hashlib

import requests

# example 1
url = 'http://httpbin.org/post'
# d = {'key1': '你好啊', 'key2': 'value2'}
# r = requests.post(url, data=d)
# print(r.text)

# example 2
# url = 'http://172.16.68.38/dynamic/notification_api.php'
data = {
    'cmd': 's',
    'c': 'New',
    'g': 's',
    'm': 'wechat',
    's': '微信接口测试',
    'salt': "1",
    't': "ChenYu@gds-services.com",
    'sign': "",
    'ct': '微信接口测试'
}
sign_field = ['cmd', 'c', 'g', 'm', 's', 'salt']
sign_values = [data[e] for e in sign_field]
sign_bytes = [e.encode('utf-8') for e in sign_values]
data['sign'] = hashlib.sha1(b"".join(sign_bytes)).hexdigest()
print(data)
r = requests.post(url, data=data)
print(r.text)
