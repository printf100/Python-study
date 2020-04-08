# -*- coding:utf-8 -*-

import pickle

score = {'name': 'kh', 'kor': 100, 'eng': 40, 'math': 60}

with open('test02.txt', 'wb') as file:  # wb : binary 타입으로 객체 자체를 write
    pickle.dump(score, file)


'''
pickling : 객체를 파일에 저장하는 것
unpickling : 파일을 객체로 빼오는 것
'''