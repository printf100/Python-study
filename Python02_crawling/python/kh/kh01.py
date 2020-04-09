# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

# kh 강사소개 크롤링하기
response = requests.get('https://www.iei.or.kr/intro/teacher.kh')

soup = BeautifulSoup(response.text, 'html.parser')

div = soup.find('div', class_='intro_list')
li = div.select('li')

for info in li:
    img = info.find('div', class_='intro_thum').find('img').get('src')
    name = info.find('p', class_='intro_name').text
    print('{} [{}]'.format(img, name))
