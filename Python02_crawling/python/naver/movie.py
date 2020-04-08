# -*- coding:utf-8 -*-

# pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(response, 'html.parser')  # url에서 받아온 string을 html 문서로 파싱
# print(soup)

movies = soup.find_all('dl', class_='lst_dsc')
# print(movies)

for movie in movies:
    title = movie.find('a').text
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))
