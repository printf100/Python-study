# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_root():
    return '<a href="/flask">FLASK</a>'


@app.route('/flask')
def hello_flask():
    return '<h1><a href="/">ROOT</a></h1>'


if __name__ == '__main__':
    app.run()
