#!/usr/bin/env python
# coding=utf-8
# 
# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/11/7
"""ES 中使用dsl 进行查询的例子。
"""

from elasticsearch import Elasticsearch

es_client = Elasticsearch("10.18.119.10:9200")

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
    "size": 500,
    "sort": [
        {
            "@timestamp": {
                "order": "desc",
                "unmapped_type": "boolean"
            }
        }
    ],
    "query": {
        "bool": {
            "must": [
                {
                    "query_string": {
                        "query": "loglevel: ERROR",
                        "analyze_wildcard": True,
                        "default_field": "*"
                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "gte": 1541260800000,
                            "lte": 1541865599999,
                            "format": "epoch_millis"
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

res = es_client.search(index="orion-phoenix-*", body=dsl3)
print(len(res))
print(res)
