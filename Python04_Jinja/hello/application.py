# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def root():
    return '''
        <a href="/hello">HELLO</a>
        <input type="button" value="HELLO" onclick="location.href='/hello/name'">
    '''
    
    
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):  # name이 없으면 None으로
    return render_template('hello.html', name=name)


@app.route('/test', methods=['post'])
def test():
    return render_template('test.html', test=request.form['command'])


if __name__ == '__main__':
    app.run('localhost', port='8585')  # http://localhost:8585/
