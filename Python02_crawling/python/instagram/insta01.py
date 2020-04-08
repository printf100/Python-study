# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# 응답되자마자 데이터를 가져오기 때문에 태그들을 못가져옴