#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/7
"""ES 中使用dsl 进行查询的例子。

注意：如果查询中使用到了日期范围查询，那么最好指明时区（通过在日期串中，或者是使用 time_zone
参数），否则若无时区信息，则会认为是 UTC 时间，即0时区的时间。

由于没有数据的关系，并未在真实的ES环境中运行，这里仅供参考
"""

from elasticsearch import Elasticsearch

es_client = Elasticsearch("172.27.110.5:9200")

dsl1 = {
    "query": {
        "term": {"loglevel.keyword": "ERROR"}
    }
}

dsl2 = {
    "query": {
        "match": {"loglevel": "ERROR"}
    }
}

dsl = {
    "query": {
        "match_all": {}
    }
}

dsl3 = {
    "size": 0,
    "query": {
        "bool": {
            "must": [
                {
                    "aggs": {
                        "request_ids": {
                            "terms": {"field": "request_ids"}
                        }
                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            'gte': '2018-11-19 18:50:10.728',
                            'lte': '2018-11-19 18:53:10.728',
                            'format': 'yyyy-MM-dd HH:mm:ss.SSS',
                            "time_zone": "+08:00"
                        }
                    }
                }
            ],
            "filter": [],
            "should": [],
            "must_not": []
        }
    }
}

res = es_client.search(index="orion-*", body=dsl3)
print(len(res))
print(res)
