# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/20
"""Test Get method in requests lib.
"""

import requests

url = 'http://10.147.20.146:80/visdata/rest/monitor/planconfig/checkplan'
params = {"checkDate": "2019-05-15"}
r = requests.get(url, params=params)
print(r.text)
print(r.status_code)
print(r.content)
print(r.json())
