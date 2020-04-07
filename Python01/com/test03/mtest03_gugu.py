# -*- coding:utf-8 -*-


# 1. for문을 사용하여 구구단 전체 출력하는 gugu() 함수를 만들자.
def gugu():
    for i in range(2, 10):
        print()
        print('< {}단 >'.format(i))
        for j in range(1, 10):
            print('{} X {} = {}'.format(i, j, i * j))


# 2. while문을 사용하여 입력된 숫자의 단만 출력하는 gugudan(x)를 만들자.
def gugudan(x):
    print()
    print('< {}단 >'.format(x))
    for i in range(1, 10):
        print('{} X {} = {}'.format(x, i, x * i))


# 3. main 만들어서 위 두 함수를 호출하자.
if __name__ == '__main__':
    gugu()
    print()
    dan = int(input('출력하고 싶은 단 : '))
    gugudan(dan)
