# -*- coding:utf-8 -*-

from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/crawling')
def crawling():
    # naver movie list를 crawling 해오자.
    response = requests.get('https://movie.naver.com/movie/running/current.nhn')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = soup.find_all('dl', class_='lst_dsc')
    
    lst = list()
    for movie in movies:
        tmp = {}
        tmp['title'] = movie.find('a').text
        tmp['star'] = movie.select('.num')[0].text
        
        lst.append(tmp)
        
    # crawling된 데이터를 dictionary에 {movies:[{title: 제목, star: 별점}, ...]} 로 저장하자.
    res_dict = {'movies':lst}
    
    res_json = json.dumps(res_dict, ensure_ascii=False)
    
    # json으로 변환하여 리턴하자
    return res_json


if __name__ == '__main__':
    app.run('localhost', port='8585')
