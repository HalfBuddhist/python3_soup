# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/25
"""time 库接口试用,
可以用以获得数字形式的时区偏移
"""

import time

# localtime, get the local time including the timezone conformed to the local
# machine
a = time.localtime()
print(a)
print(time.strftime('%Z, %z', a))

print(time.strftime("%Y-%m-%d %H:%M:%S %Z", a))  # 来获取本地化的时间。
