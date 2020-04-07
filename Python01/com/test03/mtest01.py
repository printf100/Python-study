# -*- coding:utf-8 -*-


def func01():
    pass


# 두 칸 엔터 권장
def func02():
    print('함수02 입니다.')

    
def func03():
    return '함수03 입니다.'


def func04():
    return {1:'a', 2:200}
    

if __name__ == '__main__':
    # main 함수 : 프로그램의 주 진입점
    func02()
    print(func02())  # None : 아무것도 없다 라는 뜻 (null과 비슷)
    str01 = func03()
    print(str01)
    print(func04()[1])  # key가 1인 애의 value를 가져와라
