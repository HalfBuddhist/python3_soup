# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/4/18
"""供手工写入zookeeper中的配置信息进使用。

要点：
    1. 命令行写入配置时，要客户端的编码；
    2. 如果直接将 dumps 的字符串写入，会有二次转义的情况发生，即如果有转义字符，
       认为是输入的字符，即认为是源串，相当于 python 中的 r'str', 这样就会有错误，
       应该可以这样认为，命令行中输入的都是源串。
       可以这样解释，如果 \n 是回车，那字符显示中的回车又是什么呢？
    3. 正确的输入姿势是，不要用 dumps，而是直接敲入这个字典 (正确来讲是，json 对象)，
       输入时将 None 转为 null, False 转为 false, True 转化为 true。
"""

import json

import ujson

import json5

config2 = {
    'send_by_gds_api': False,
    'gds_api_address': 'http://172.16.68.38/dynamic/notification_api.php',
    'gds_api_m': 'all',
    'gds_api_s': '测试',
    'gds_api_t': 'liuqingwei;tianguicheng'
}

config = {"request_id": 1234,
           "job": {
               "tag": "job-567",
               "val": 8,
               "factor": 8
           }
}

config1 = {
    "cow_circuit": {
        "#1": {
            "status": "on",
            "f_fan": [30, 50],
            "f_cow_pump": [30, 50]
        },
        "#2": {
            "status": "on",
            "f_fan": [30, 50],
            "f_cow_pump": [30, 50]
        },
        "#3": {
            "status": "on",
            "f_fan": [30, 50],
            "f_cow_pump": [30, 50]
        },
        "#4": {
            "status": "off",
            "f_fan": [30, 50],
            "f_cow_pump": [30, 50]
        },
        "#5": {
            "status": "off",
            "f_fan": [30, 50],
            "f_cow_pump": [30, 50]
        },
        "#6": {
            "status": "off",
            "f_fan": [30, 50],
            "f_cow_pump": [30, 50]
        }
    },
    "chiller": {
        "#1": {
            "t_cow_in": [17.5, 30.0],
            "p_condenser": [530.0, 900.0],
            "f_chiller": [35.0, 100.0]
        },
        "#2": {
            "t_cow_in": [17.5, 30.0],
            "p_condenser": [530.0, 900.0],
            "f_chiller": [35.0, 100.0]
        },
        "#3": {
            "t_cow_in": [17.5, 30.0],
            "p_condenser": [530.0, 900.0],
            "f_chiller": [35.0, 100.0]
        },
        "#4": {
            "t_cow_in": [17.5, 30.0],
            "p_condenser": [530.0, 900.0],
            "f_chiller": [35.0, 100.0]
        },
        "#5": {
            "t_cow_in": [17.5, 30.0],
            "p_condenser": [530.0, 900.0],
            "f_chiller": [35.0, 100.0]
        },
        "#6": {
            "t_cow_in": [17.5, 30.0],
            "p_condenser": [530.0, 900.0],
            "f_chiller": [35.0, 100.0]
        }
    }
}


json_str = json.dumps(config, ensure_ascii=False)
print("dict：\n", config)
print("repr：\n", repr(config))
print("dumps：\n", json_str)
print("encode：\n", json_str.encode())
print("utf-8 encode：\n", json_str.encode('utf-8'))

# loadt.json
a = json.loads(json_str)
print(a)


print('#' * 20)
# with open('sz_contraints_template.json', 'r') as fp:
with open('master_sz2.json', 'r') as fp:
    a = json5.load(fp)
print("dict：\n", a)
print('-' * 20)
print("repr：\n", repr(a))
print('-' * 20)
print("dumps：\n", json.dumps(a, ensure_ascii=False))
print('-' * 20)
print("encode：\n", json.dumps(a, ensure_ascii=False).encode())
print('-' * 20)
print("utf-8 encode：\n", json.dumps(a, ensure_ascii=False).encode('utf-8'))
