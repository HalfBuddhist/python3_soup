# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: Qingwei <linquan@chuangxin.com>
# Date:   2018/12/19
# coding=utf-8

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True)
# bot = Bot()
# print(bot.chats())
bot.self.send('Hello World!')
bot.file_helper.send('Hello World!')
