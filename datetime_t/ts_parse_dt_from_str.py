# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/25
"""parse 时，使用%f macro 来解析对应的浮点数毫秒部分。

time.strptime 形成的 struct_time 没有保存毫秒部分, 尽管可以识别
datetime.strptime 既可以识别，又可以保存毫秒。
"""
import time
from datetime import datetime

print("time.strptime")
t = time.strptime('30/03/09 16:31:32.123', '%d/%m/%y %H:%M:%S.%f')
print(t, str(t), type(t))


print("datetime.strptime")
a = datetime.strptime('30/03/09 16:31:32.123456', '%d/%m/%y %H:%M:%S.%f')
print(a)
print(a.strftime("%d/%m/%y %H:%M:%S.%f %z"))
print(a.microsecond)
