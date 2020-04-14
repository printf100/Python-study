# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.db
score = db.score

aggr = score.aggregate([
            {'$match': {'kor': {'$gt': 50}}},
            {'$group': {'_id': 'kor', 'sum': {'$sum': '$kor'}}}
        ])

print(aggr)

pprint.pprint(list(aggr))