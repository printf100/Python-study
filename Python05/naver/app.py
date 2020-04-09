# -*- coding:utf-8 -*-

from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r'*':{'origins':'*'}})


@app.route('/')
def root():
    return render_template('index.html')


lst = list()


@app.route('/crawling')
def crawling():
    # naver movie list를 crawling 해오자.
    response = requests.get('https://movie.naver.com/movie/running/current.nhn')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = soup.find_all('dl', class_='lst_dsc')
    
    for movie in movies:
        title = movie.find('a').text
        star = movie.find('span', class_='num').text
        
        tmp = {}
        tmp['title'] = title
        tmp['star'] = star
        
        lst.append(tmp)
    
    # crawling된 데이터를 dictionary에 {movies:[{title: 제목, star: 별점}, ...]} 로 저장하자.
    res = {}
    res['movies'] = lst
    
    res_json = json.dumps(res, ensure_ascii=False)
    
    # json으로 변환하여 리턴하자        
    return res_json


if __name__ == '__main__':
    app.run('localhost', port='8585')
