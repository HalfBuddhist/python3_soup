# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/23
"""pytz 相关测试接口测试
"""

from datetime import datetime

from pytz import reference
from pytz import timezone
from pytz import utc

# 初始化为当前时间，或者指定时间
today = datetime.now()
insummer = datetime(2009, 8, 15, 10, 0, 0)
print(repr(today), repr(insummer))

# 获得当前系统时区，时区 ID
localtime = reference.LocalTimezone()
print(localtime, repr(localtime))
print(localtime.tzname(today))
print(localtime.tzname(insummer))
print(repr(today), repr(insummer))
print(today.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
print(insummer.strftime("%Y-%m-%d %H:%M:%S.%f %z"))


# form the tz by id
cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')
print(cst_tz, type(cst_tz))
print(utc_tz, type(utc_tz))


now = datetime.now().replace(tzinfo=cst_tz)  # 不建议
print(now.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
utctime = now.astimezone(utc)
print(utctime.strftime("%Y-%m-%d %H:%M:%S.%f %z"))

local_dt = cst_tz.localize(datetime.now(), is_dst=None)  # 正确
print(local_dt, type(local_dt))
print(local_dt.strftime("%Y-%m-%d %H:%M:%S.%f %z"))


utcnow = datetime.utcnow()
print(utcnow.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
utcnow = utcnow.replace(tzinfo=utc_tz)
china = utcnow.astimezone(cst_tz)
print(utcnow.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
print(china.strftime("%Y-%m-%d %H:%M:%S.%f %z"))

# 不幸的是，使用标准datetime构造函数的tzinfo参数对于许多时区不适用于pytz,
# 不建议
t = datetime(2013, 11, 22, hour=11, minute=0, tzinfo=timezone('Europe/Warsaw'))
print(t.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
tt = t.astimezone(utc).astimezone(timezone('Europe/Warsaw'))
print(tt.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
# 建议
t = timezone('Europe/Warsaw').localize(datetime(2013, 5, 11, hour=11, minute=0))
print(t.strftime("%Y-%m-%d %H:%M:%S.%f %z"))
