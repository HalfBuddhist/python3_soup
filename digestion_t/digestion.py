# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/4/18
"""
"""

import hashlib

# sha1
res = hashlib.sha1("admin1234".encode('utf-8')).hexdigest()
print(res, type(res))
res = hashlib.sha1("sNewswechat通知接口测试1".encode('utf-8')).hexdigest()
print(res, type(res))


# base64
import base64
message = 'python is fun'
msg_bytes = message.encode('utf-8')
b64_bytes = base64.b64encode(msg_bytes)
print(b64_bytes, b64_bytes.decode("utf-8"))


# htpasswd example: htpasswd -nbs admin admin1234
sha_digest = hashlib.sha1("admin1234".encode('utf-8')).digest()
b64_bytes = base64.b64encode(sha_digest)
print(b64_bytes, b64_bytes.decode("utf-8"))
