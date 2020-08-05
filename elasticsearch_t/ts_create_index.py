# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@ainnovation.com>
# Date:   2019/5/22
"""测试使用文档映射来创建索引

1. 还测试了检索，更新文档，刷新索引，检索文档的接口，常用 ES 工作流。
2. 测试一下以下划线开头的域，在查询是否默认来返回, 是有返回的, 以前应该是 BUG 引起的误解。
"""

from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

es_client = Elasticsearch("cxgc.me.lan:9200")
index_client = IndicesClient(es_client)

body = {
    "mappings": {
        "doc": {
            "dynamic_date_formats": [
                "strict_date_time",
                "strict_date_optional_time",
                "yyyy/MM/dd HH:mm:ss Z||yyyy/MM/dd Z"],
            "numeric_detection": True,
            "properties": {
                "@timestamp": {
                    "type": "date",
                    "format": "strict_date_optional_time||epoch_millis"
                },
                "modify_datetime": {  # todo, format?
                    "type": "date",
                    "format": "strict_date_optional_time||epoch_millis"
                },
                "last_seen_id": {
                    "type": "keyword"
                },
                "controlStatus": {
                    "type": "keyword"
                }
            }
        }
    }
}

# create index
if not index_client.exists(index="test-index"):
    index_client.create(index="test-index",
                        body=body)
    print("complished index create.")

# write a time
doc = {
    "@timestamp": "2019-09-09T05:09:09.000Z",
    "timestamp1": "2019-05-22T01:30:00.000+0000",
    "modify_datetime": "2019-05-22T01:30:00.000+0800",
    "last_seen_id": "q51R32oBilhNrSf_YYbg",
    "controlStatus": "AI",
    "tiangc": "hello world",
}
doc['_cnt_day_avg'] = 444  # test the '_' starting field insert and query.
res = es_client.index(index="test-index", doc_type='doc', body=doc)
print(res)
index_client.refresh(index="test-index")

# find all
res = es_client.search(index="test-index", body={"query": {"match_all": {}}})
print(res)
#
# query = {
#     "query": {
#         "match": {
#             "tiangc": "hello world"
#         }
#     }
# }
# res = es_client.search(index="test-index", body=query)
# print(res)
# print('#' * 30)
#
# res = es_client.get(index='test-index', doc_type='doc',
#                     id='HJ6K32oBilhNrSf_MtRt')
# print(res)
#
# print('#' * 30)
#
# newbody = {
#     'doc': {
#         "tiangc": "hello kitty",
#     }
# }
# es_client.update(index='test-index', doc_type='doc', id='HJ6K32oBilhNrSf_MtRt',
#                  body=newbody)
#
# index_client.refresh(index="test-index")
#
# res = es_client.get(index='test-index', doc_type='doc',
#                     id='HJ6K32oBilhNrSf_MtRt')
# print(res)
