# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqingwei <liuqingwei@chuangxin.com>
# Date:   2018/7/2
# coding=utf-8
"""free test
"""

a = {
    "sort": [
        {
            "@timestamp": {
                "order": "asc",
                "unmapped_type": "boolean"
            }
        }
    ],
    "_source":
        ['S0E2A24',
         'S0E1A6',
         'S1E9A31',
         'S1E9A32',
         'S1E9A33',
         'S1E9A34',
         'S1E9A35',
         'S0E32A12',
         'S0E32A11',
         'S0E2A25',
         'S0E2A48',
         'S0E2A50',
         'S2E27A30',
         'S2E58A30',
         'S2E32A30',
         'S2E53A30',
         'S4E15A30',
         'S4E46A30',
         'S4E20A30',
         'S4E40A30',
         'S2E24A30',
         'S2E55A30',
         'S2E29A30',
         'S2E50A30',
         'S4E12A30',
         'S4E42A30',
         'S4E17A30',
         'S4E37A30',
         'S2E46A30',
         'S2E26A30',
         'S2E38A30',
         'S2E57A30',
         'S2E52A30',
         'S2E31A30',
         'S4E45A30',
         'S4E14A30',
         'S4E25A30',
         'S4E44A30',
         'S4E19A30',
         'S4E39A30',
         'S2E23A30',
         'S2E54A30',
         'S2E49A30',
         'S2E28A30',
         'S4E11A30',
         'S4E41A30',
         'S4E16A30',
         'S4E36A30',
         'S2E25A30',
         'S2E56A30',
         'S2E30A30',
         'S2E51A30',
         'S4E13A30',
         'S4E43A30',
         'S4E18A30',
         'S4E38A30',
         'S0E2A65',
         'S0E2A66', 'S0E2A67', 'S0E2A68', 'S0E2A69', 'S0E2A27', 'S0E2A28',
         'S0E2A29',
         'S0E2A30', 'S0E2A31', 'S0E2A32', 'S0E2A33',
         'S0E2A34', 'S0E2A42', 'S0E2A43', "@timestamp"],
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "2019-05-0800:00:00.000",
                            "lt": "2019-06-2823:59:59.999",
                            "format": "yyyy-MM-ddHH:mm:ss.SSS",
                            "time_zone": "+08:00"
                        }
                    }
                }
            ]
        }
    }
}

import ujson
import json

print(ujson.dumps(ujson.dumps(a, ensure_ascii=False)))
print(json.dumps(json.dumps(a, ensure_ascii=False)))
