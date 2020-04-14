# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)

db = client['test']
# db = client.test

score = db['score']
# score = db.score

result = score.find()
for res in result:
    print(res)
