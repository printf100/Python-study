# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.test
score = db.score

cursor = score.find()
print(cursor)

for doc in cursor:
    pprint.pprint(doc)
    
print("-------------------------")

hong = score.find({"name":"홍길동"})
pprint.pprint(hong)
for doc in hong:
    print(doc)

print("-------------------------")

cho = score.find_one({"name":"조세호"})
pprint.pprint(cho)

print("-------------------------")

print("document의 총 갯수 : ", score.count_documents({}))

print("-------------------------")

# 국어 점수가 70점보다 높은 사람만 출력
kor = score.find({"kor": {"$gt": 70}})
for doc in kor:
    print(doc)
