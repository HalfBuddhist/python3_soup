# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2019/3/1
"""使用 scroll api 来 获得所有满足条件的数据。

docker run --name scroll  \
  --entrypoint=""  \
  -v /home/qz/lqw/test:/serving_demo   \
  -d harbor.gds.com/control_predict/serving:build_0515_f834998  \
  sh -c "python scroll_fetch_large.py --es_path=172.31.35.110:9200  \
   --index_pattern=sensor-sz2  \
  --file_path=/home/qz/lqw/test/res.csv \
  --query_dsl={\"query\": { \"match_all\": {} }"

docker run --name scroll --rm  \
  --entrypoint=""  \
  -v /home/qz/lqw/test:/serving_demo   \
  harbor.gds.com/control_predict/serving:build_0614_0337c7e  \
  sh -c 'python scroll_fetch_large.py --es_path=172.31.35.110:9200  \
   --index_pattern=sensor-sz2  \
  --file_path=/serving_demo/res_enh.csv \
  --query_dsl={\"sort\":[{\"@timestamp\":{\"order\":\"asc\",\"unmapped_type\":\"boolean\"}}],\"_source\":[\"S0E2A24\",\"S0E1A6\",\"S1E9A31\",\"S1E9A32\",\"S1E9A33\",\"S1E9A34\",\"S1E9A35\",\"S0E32A12\",\"S0E32A11\",\"S0E2A25\",\"S0E2A48\",\"S0E2A50\",\"S2E27A30\",\"S2E58A30\",\"S2E32A30\",\"S2E53A30\",\"S4E15A30\",\"S4E46A30\",\"S4E20A30\",\"S4E40A30\",\"S2E24A30\",\"S2E55A30\",\"S2E29A30\",\"S2E50A30\",\"S4E12A30\",\"S4E42A30\",\"S4E17A30\",\"S4E37A30\",\"S2E46A30\",\"S2E26A30\",\"S2E38A30\",\"S2E57A30\",\"S2E52A30\",\"S2E31A30\",\"S4E45A30\",\"S4E14A30\",\"S4E25A30\",\"S4E44A30\",\"S4E19A30\",\"S4E39A30\",\"S2E23A30\",\"S2E54A30\",\"S2E49A30\",\"S2E28A30\",\"S4E11A30\",\"S4E41A30\",\"S4E16A30\",\"S4E36A30\",\"S2E25A30\",\"S2E56A30\",\"S2E30A30\",\"S2E51A30\",\"S4E13A30\",\"S4E43A30\",\"S4E18A30\",\"S4E38A30\",\"S0E2A65\",\"S0E2A66\",\"S0E2A67\",\"S0E2A68\",\"S0E2A69\",\"S0E2A27\",\"S0E2A28\",\"S0E2A29\",\"S0E2A30\",\"S0E2A31\",\"S0E2A32\",\"S0E2A33\",\"S0E2A34\",\"S0E2A42\",\"S0E2A43\",\"@timestamp\"],\"query\":{\"bool\":{\"must\":[{\"range\":{\"@timestamp\":{\"gte\":\"2019-05-0800:00:00.000\",\"lt\":\"2019-06-2823:59:59.999\",\"format\":\"yyyy-MM-ddHH:mm:ss.SSS\",\"time_zone\":\"+08:00\"}}}]}}}'

docker run --name scroll --rm  \
  --entrypoint=""  \
  -v /home/qz/lqw/test:/serving_demo   \
  harbor.gds.com/control_predict/serving:build_0604_872d482  \
  sh -c 'python scroll_fetch_large.py --es_path=172.31.35.110:9200  \
   --index_pattern=sensor-sz2  \
  --file_path=/serving_demo/res_enh.csv \
  --query_dsl={\"sort\":[{\"@timestamp\":{\"order\":\"asc\",\"unmapped_type\":\"boolean\"}}],\"_source\":[\"S0E2A24\",\"S0E1A6\",\"S1E9A31\",\"S1E9A32\",\"S1E9A33\",\"S1E9A34\",\"S1E9A35\",\"S0E32A12\",\"S0E32A11\",\"S0E2A25\",\"S0E2A48\",\"S0E2A50\",\"S2E27A30\",\"S2E58A30\",\"S2E32A30\",\"S2E53A30\",\"S4E15A30\",\"S4E46A30\",\"S4E20A30\",\"S4E40A30\",\"S2E24A30\",\"S2E55A30\",\"S2E29A30\",\"S2E50A30\",\"S4E12A30\",\"S4E42A30\",\"S4E17A30\",\"S4E37A30\",\"S2E46A30\",\"S2E26A30\",\"S2E38A30\",\"S2E57A30\",\"S2E52A30\",\"S2E31A30\",\"S4E45A30\",\"S4E14A30\",\"S4E25A30\",\"S4E44A30\",\"S4E19A30\",\"S4E39A30\",\"S2E23A30\",\"S2E54A30\",\"S2E49A30\",\"S2E28A30\",\"S4E11A30\",\"S4E41A30\",\"S4E16A30\",\"S4E36A30\",\"S2E25A30\",\"S2E56A30\",\"S2E30A30\",\"S2E51A30\",\"S4E13A30\",\"S4E43A30\",\"S4E18A30\",\"S4E38A30\",\"@timestamp\"],\"query\":{\"bool\":{\"must\":[{\"range\":{\"@timestamp\":{\"gte\":\"2019-05-0800:00:00.000\",\"lt\":\"2019-06-2823:59:59.999\",\"format\":\"yyyy-MM-ddHH:mm:ss.SSS\",\"time_zone\":\"+08:00\"}}}]}}}'

docker run --name scroll --rm  \
  --entrypoint=""  \
  -v /home/qz/lqw/test:/serving_demo   \
  harbor.gds.com/control_predict/serving:build_0625_f5fbaf4  \
  sh -c 'python scroll_fetch_large.py --es_path=172.31.35.110:9200  \
   --index_pattern=sensor-sz2  \
  --file_path=/serving_demo/sensor_23_29.csv \
  --query_dsl={\"sort\":[{\"@timestamp\":{\"order\":\"asc\",\"unmapped_type\":\"boolean\"}}],\"query\":{\"bool\":{\"must\":[{\"range\":{\"@timestamp\":{\"gte\":\"2019-07-2311:00:00.000\",\"lt\":\"2019-07-2917:00:00.000\",\"format\":\"yyyy-MM-ddHH:mm:ss.SSS\",\"time_zone\":\"+08:00\"}}}]}}}'

docker run --name scroll --rm  \
  --entrypoint=""  \
  -v /data/lqw/tools:/serving_demo  \
  harbor.ainnovation.com/gds/serving:build_20190827  \
  sh -c 'python scroll_fetch_large.py --es_path=10.68.67.205:9200  \
  --index_pattern=sensor-bj2  \
  --file_path=/serving_demo/sensor_bj2_0809_now.csv  \
  --query_dsl={\"sort\":[{\"@timestamp\":{\"order\":\"asc\",\"unmapped_type\":\"boolean\"}}],\"query\":{\"bool\":{\"must\":[{\"range\":{\"@timestamp\":{\"gte\":\"2019-08-0917:30:00.000\",\"lt\":\"2019-10-2917:00:00.000\",\"format\":\"yyyy-MM-ddHH:mm:ss.SSS\",\"time_zone\":\"+08:00\"}}}]}}}'

docker run --name scroll --rm  \
  --entrypoint=""  \
  -v /home/liuqw/workspace/python3_soup/elasticsearch_t:/serving_demo  \
  harbor.ainnovation.com/gds/serving:build_20190827  \
  sh -c 'python scroll_fetch_large.py --es_path=10.18.98.44:9200  \
  --index_pattern=orion-phoenix-*  \
  --file_path=/serving_demo/error.csv  \
  --query_dsl={\"_source\":[\"err\",\"fields.role\",\"filename\",\"lineno\",\"@timestamp\"],\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"query\":{\"bool\":{\"must\":[{\"range\":{\"@timestamp\":{\"gte\":\"2010-12-15\ 00:00:00.000\",\"lt\":\"2020-01-10\ 00:00:00.000\",\"format\":\"yyyy-MM-dd\ HH:mm:ss.SSS\",\"time_zone\":\"+08:00\"}}},{\"term\":{\"loglevel.keyword\":\"ERROR\"}}],\"filter\":[],\"should\":[],\"must_not\":[]}}}'

docker run --name scroll --rm  \
  --entrypoint=""  \
  -v /data/lqw:/serving_demo  \
  harbor.ainnovation.com/gds/serving:build_20190827  \
  sh -c 'python scroll_fetch_large.py --es_path=10.141.90.192:9200  \
  --index_pattern=orion-phoenix-*  \
  --file_path=/serving_demo/error.csv  \
  --query_dsl={\"_source\":[\"err\",\"fields.role\",\"filename\",\"lineno\",\"@timestamp\"],\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"query\":{\"bool\":{\"must\":[{\"range\":{\"@timestamp\":{\"gte\":\"2010-12-15\ 00:00:00.000\",\"lt\":\"2020-01-10\ 00:00:00.000\",\"format\":\"yyyy-MM-dd\ HH:mm:ss.SSS\",\"time_zone\":\"+08:00\"}}},{\"term\":{\"loglevel.keyword\":\"ERROR\"}}],\"filter\":[],\"should\":[],\"must_not\":[]}}}'

"""

import logging
import logging.config
import sys

import gflags
import ujson
from elasticsearch import Elasticsearch
from elasticsearch import helpers

gflags.DEFINE_string("es_path", "127.0.0.1:9200", "path of the es")
gflags.DEFINE_string("index_pattern", "orion-changan-s1-*",
                     "es index pattern to scroll on")
gflags.DEFINE_string("file_path", "/tmp/output.csv", "output of the scroll res")
gflags.DEFINE_string("query_dsl", '{\"query\": { \"match_all\": {} }',
                     "end time")

FLAGS = gflags.FLAGS


class ElasticSearchWrapper(object):

    def __init__(self, client):
        self._client = client

    def scroll_data_in_duration(self, dsl):
        """Scroll on query
        :param dsl:
        :return: a generator
        """
        result = helpers.scan(client=self._client, query=dsl,
                              index=FLAGS.index_pattern)
        return result


def main(argv=None):
    FLAGS(argv)
    es_client = Elasticsearch(FLAGS.es_path)
    wrapper = ElasticSearchWrapper(es_client)
    logging.basicConfig()
    logger = logging.getLogger()

    logger.info("dsl_str=%s" % FLAGS.query_dsl)
    dsl = ujson.loads(FLAGS.query_dsl)
    logger.info("query_dsl=%s" % dsl)
    res = wrapper.scroll_data_in_duration(dsl)
    with open(FLAGS.file_path, 'w') as fp:
        # write the header
        if '_source' in dsl:
            headers = dsl['_source']
            fp.write("|".join(headers) + '\n')
            cnt = 0
        else:
            first_res = next(res)
            headers = [col for col in first_res['_source'].keys()]
            fp.write("|".join(headers) + '\n')
            row_data = [str(first_res['_source'][col])
                        if col in first_res['_source'] else 'nan'
                        for col in headers]
            fp.write("|".join(row_data) + "\n")
            cnt = 1
        for r in res:
            cnt += 1
            row_data = []
            for col in headers:
                if col in r['_source']:
                    row_data.append(str(r['_source'][col]).
                        replace('\n', ' ').replace('|', ' ').replace('\r', ' '))
                # elif '.' in col:
                #     col_seq = col.split('.')
                #     t_dict = r
                #     for iter_col in col_seq:
                #       t_dict = t_dict[iter_col]
                #     row_data.append(str(t_dict))
                else:
                    row_data.append('nan')
            # row_data.append(r['_id'])
            # row_data.append(r['_source'][''])
            fp.write("|".join(row_data) + "\n")

    logger.info("Found %s response doc, and write it to %s." % (
        cnt, FLAGS.file_path))


if __name__ == "__main__":
    main(sys.argv)
