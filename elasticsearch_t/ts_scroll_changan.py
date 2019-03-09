# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/1
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
        "ids",
        "98AE1666E71A708FE71788CA2CD209F3,720657EA0D115486FFFD543580CEEA40",
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
        self._dsl_response = {
            "sort": [
                {
                    "@timestamp": {
                        "order": "desc",
                        "unmapped_type": "boolean"
                    }
                }
            ],
            "_source": [
                "request_id",
                "response_json.data.destination_poi",
                "@timestamp"
            ],
            "query": {
                "bool": {
                    "must": [
                        {
                            "term": {
                                "response_json.code": 0
                            }
                        },
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "2019-02-28 00:00:00.000",
                                    "lte": "2019-02-28 23:59:59.999",
                                    "format": "yyyy-MM-dd HH:mm:ss.SSS",
                                    "time_zone": get_time_zone_in_es_fmt()
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
        self._dsl_request = {
            "size": 5000,
            "_source": [
                "request_id",
                "request_json.data.current_poi",
                "request_json.data.current_time",
                "request_json.data.car_id",
                "@timestamp"
            ],
            "query": {
                "bool": {
                    "must": [
                        {
                            "terms": {
                                "request_id.keyword": []
                            }
                        },
                        {
                            "exists": {
                                "field": "request_json"
                            }
                        }
                    ],
                    "filter": [],
                    "should": [],
                    "must_not": []
                }
            }
        }

    def get_response_data_in_duration(self, stime, etime):
        self._dsl_response['query']['bool']['must'][1]['range'][
            '@timestamp']['gte'] = stime
        self._dsl_response['query']['bool']['must'][1]['range'][
            '@timestamp']['lte'] = etime
        result = helpers.scan(client=self._client, query=self._dsl_response,
                              index="orion-changan-s1-*")
        return result

    def get_request_by_id(self, ids):
        if len(ids) == 0 or len(ids) >= 5000:
            raise ElasticSearchWrapperException(
                    "Wrong id array, too long or empty.")
        self._dsl_request['query']['bool']['must'][0]['terms'][
            'request_id.keyword'] = ids
        res = self._client.search(
                index="orion-changan-s1-*", body=self._dsl_request)
        return res


def main(argv=None):
    FLAGS(argv)
    es_client = Elasticsearch(FLAGS.es_path)
    wrapper = ElasticSearchWrapper(es_client)
    # res is a generator
    res = wrapper.get_response_data_in_duration(FLAGS.stime, FLAGS.etime)
    i = 0
    with open("response.json", "w") as fp:
        for r in res:
            i += 1
            fp.write(str(r))
    print("Found %s response doc." % i)

    ids = FLAGS.ids.split(",")
    res2 = wrapper.get_request_by_id(ids)
    print(len(res2['hits']['hits']))
    with open("request.json", "w") as fp:
        fp.write(str(res2))
    print("Finished.")


if __name__ == "__main__":
    main(sys.argv)
