# -*- coding: utf-8 -*-
# author: huihui
# date: 2019/12/16 1:26 下午 

'''
使用原始语料的title字段进行测试
'''

from elasticsearch import Elasticsearch
import json

from my_config import hosts

es = Elasticsearch(hosts=hosts)

index_name = "kuakua_table"
doc_type = "comment"
file_name = "data/content_file.txt"


def index_data():
    json_data = json.load(open(file_name))
    print(len(json_data))

    _id = 1
    for doc in json_data:
        res = es.index(index=index_name, doc_type=doc_type, id=_id, body=doc)
        print("[{}/{}] {} ".format(_id, len(json_data), res['result']))

        # res = es.get(index=index_name, doc_type=doc_type, id=_id)
        # print(res['_source'])

        _id += 1

    es.indices.refresh(index=index_name)


def query_data(query):
    body = {
        "query": {
            "match": {
                "title": query
            }
        }
    }

    result = es.search(index=index_name, doc_type=doc_type, body=body)
    hits = result['hits']['hits']
    for hit in hits:
        print("{} {}".format(hit['_score'], hit['_source']['title']))


if __name__ == "__main__":
    query = '学习好辛苦哦'
    query = '科研好累，能不能换专业？求导师理解！！'
    query = '回归20年来，“一国两制”的成功实践，让澳门发生了翻天覆地的变化。'
    query = '怎样才能发表论文？！'
    print(query)
    print()
    query_data(query)
