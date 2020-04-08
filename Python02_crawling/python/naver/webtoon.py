# -*- coding:utf-8 -*-

# pip install requests

import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=wed')

soup = BeautifulSoup(response.text, 'html.parser')

webtoon_list = soup.find('ul', class_='img_list')

dl = webtoon_list.select('dl')  # list 형식

lst = list()
for chd in dl:
    title = chd.find('a').text
    star = chd.find('strong').text

    # json 형식으로 담기    
    tmp = {}
    tmp['title'] = title
    tmp['star'] = star

    lst.append(tmp)
    
res = {}
res['webtoons'] = lst

res_json = json.dumps(res, ensure_ascii=False)
print(res_json)

with open('webtoons.json', 'w', encoding='utf-8') as file:
    file.write(res_json)
