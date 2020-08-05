# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/23
"""转换时区
datetime.replace 返回修改时区后时间，期间时间并不做级联修改。
datetime.astimezone 同上，时间做级联修改。

datetime.now() 得到的 datetime 虽然是本地机器上的时区所对应的当前时间，
但是在对象中并没有包含 timezone 信息， 虽然repalce方法或者astimezone 方法来
赋值与改变。

同样，datetime.utcnow() 得到的 datetime 是 UTC 0时区所对应的当前时间，
但是在对象中并没有包含 timezone 信息, 相关的域 tzinfo 值为 None，
虽然repalce方法或者astimezone 方法来赋值与改变。

astimezone 方法为转化为相应时区的时间，如果参数 tz为 None, 则置为当前时区。

"""

from datetime import datetime, timezone, timedelta
import pytz
from pytz import timezone as tz

dt = datetime.utcnow()
print(dt)
dt = dt.replace(tzinfo=timezone.utc)
print(dt)
tzutc_8 = timezone(timedelta(hours=8, minutes=10))
local_dt = dt.astimezone(tzutc_8)
print(local_dt)


utc_dt = datetime.utcnow()
print(utc_dt)
print(utc_dt.strftime("%d/%m/%y %H:%M:%S.%f %z"))
print(utc_dt.tzinfo)
print(utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None))

# 使用pytz
from pytz import timezone
utc_now = datetime.utcnow()
print(utc_now, utc_now.tzinfo)
tzchina = timezone('Asia/Shanghai')
print(tzchina)
utc = timezone('UTC')
dt_cn = utc_now.replace(tzinfo=utc).astimezone(tzchina)
print(dt_cn, type(dt_cn))
print(dt_cn.strftime("%d/%m/%y %H:%M:%S.%f %z"))

# django timezone convertion.
from django.utils.timezone import utc
from django.utils.timezone import localtime
now = datetime.datetime.utcnow().replace(tzinfo=utc)
localtime(now)
# datetime.datetime(2013, 12, 5, 0, 3, 13, 122000, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)
