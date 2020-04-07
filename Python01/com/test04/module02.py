# -*- coding:utf-8 -*-

# pip install numpy -> 수치해석
# pip install matplotlib -> 그래프 그리는 라이브러리

import numpy as np
import matplotlib.pyplot as plt
import random


def plt01():
    x = np.arange(0, 11)
    y = x
    
    plt.plot(x, y)

    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.legend(['y = x'])

    plt.show()
    
    
def plt02():
    y = [random.randint(0, 10) for i in range(10)]
    x = range(10)
    
    plt.bar(x, y)
    
    plt.xticks(range(11))
    plt.yticks(range(11))
    
    plt.show()
    
    
def plt03():
    data = [random.randint(100, 1000) for i in range(4)]    # 4번 랜덤값을 만든다.
    
    plt.pie(data)
    
    category = ['first', 'second', 'third', 'fourth']
    plt.legend(category)
    
    plt.show()

    
if __name__ == '__main__':
    plt03()
