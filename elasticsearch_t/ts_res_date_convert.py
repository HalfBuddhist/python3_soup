#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/7
"""ES 中日期返回的还是如『2019-02-25T10:25:54.815Z』这种格式的字符串。
"""

from elasticsearch import Elasticsearch

es_client = Elasticsearch("ubuntu-qz:9200")

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
    "size": 1,
    "query": {
        "match_all": {}
    }
}

dsl3 = {
    "size": 1,
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

res = es_client.search(index="orion-phoenix-train_worker-2019.02.25", body=dsl)
print(len(res))
print(res)
a = res['hits']['hits'][0]['_source']['@timestamp']
print(a, type(a))
