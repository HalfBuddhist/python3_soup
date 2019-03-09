# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/1
#
# Author: denghongwei <denghongwei@chuangxin.com>
# Date: 2019-03-05
"""使用 scroll api 来 获得所有满足条件的response数据。
"""
import sys
import time

import gflags
from elasticsearch import Elasticsearch
from elasticsearch import helpers

gflags.DEFINE_string("es_path", "127.0.0.1:9200", "path of the es")
gflags.DEFINE_string("stime", "2019-02-28 00:00:00.000", "start time")
gflags.DEFINE_string("etime", "2019-02-28 23:59:59.999", "end time")
gflags.DEFINE_string(
    "ids", "98AE1666E71A708FE71788CA2CD209F3,720657EA0D115486FFFD543580CEEA40",
    "end time")

FLAGS = gflags.FLAGS


def get_time_zone_in_es_fmt():
    time_zone = time.strftime('%z', time.localtime())
    time_zone_es_fmt = time_zone[:-2] + ":" + time_zone[-2:]
    return time_zone_es_fmt


class ElasticSearchWrapperException(Exception):
    pass


class ElasticSearchWrapper(object):

    def __init__(self, client):
        self._client = client
        self._response_source = [
            "request_id", "response_json.data.destination_poi", "@timestamp"
        ]
        self._request_source = [
            "request_id", "request_json.data.current_poi",
            "request_json.data.current_time", "request_json.data.car_id",
            "@timestamp"
        ]
        self._sort_query = {
            "sort": [{
                "@timestamp": {
                    "order": "desc",
                    "unmapped_type": "boolean"
                }
            }]
        }

    def _basic_query(self, doc_type="request"):
        assert doc_type in ["request", "response"]
        if doc_type == "request":
            source = self._request_source
            field = "request_json"
        elif doc_type == "response":
            source = self._response_source
            field = "response_json"
        query = {
            "_source": source,
            "query": {
                "bool": {
                    "must": [{
                        "exists": {
                            "field": field
                        }
                    }]
                }
            }
        }
        return query

    def _assemble_query_by_duration(self, doc_type, stime, etime):
        query = self._basic_query(doc_type)
        time_query = {
            "range": {
                "@timestamp": {
                    "gte": stime,
                    "lte": etime,
                    "format": "yyyy-MM-dd HH:mm:ss.SSS",
                    "time_zone": get_time_zone_in_es_fmt()
                }
            }
        }
        query["query"]["bool"]["must"].append(time_query)
        return query

    def _assemble_query_by_id(self, doc_type, ids):
        query = self._basic_query(doc_type)
        id_query = {"terms": {"request_id.keyword": ids}}
        query["query"]["bool"]["must"].append(id_query)
        return query

    def get_doc_in_duration(self, doc_type, stime, etime):
        query = self._assemble_query_by_duration(doc_type, stime, etime)
        result = helpers.scan(
            client=self._client, query=query, index="orion-changan-s1-*")
        return result

    def get_doc_by_id(self, doc_type, ids):
        if len(ids) == 0 or len(ids) >= 5000:
            raise ElasticSearchWrapperException(
                "Wrong id array, too long or empty.")
        query = self._assemble_query_by_id(doc_type, ids)
        res = self._client.search(index="orion-changan-s1-*", body=query)
        return res


def main(argv=None):
    FLAGS(argv)
    es_client = Elasticsearch(FLAGS.es_path)
    wrapper = ElasticSearchWrapper(es_client)
    # res is a generator
    res = wrapper.get_doc_in_duration("response", FLAGS.stime, FLAGS.etime)
    i = 0
    with open("response.json", "w") as fp:
        for r in res:
            i += 1
            fp.write(str(r))
    print("Found %s response doc." % i)

    ids = FLAGS.ids.split(",")
    res2 = wrapper.get_doc_by_id("request", ids)
    print(len(res2['hits']['hits']))
    with open("request.json", "w") as fp:
        fp.write(str(res2))
    print("Finished.")


if __name__ == "__main__":
    main(sys.argv)
