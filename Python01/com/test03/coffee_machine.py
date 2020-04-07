# -*- coding:utf-8 -*-


def coffee(cup, money):
    # 잔돈 계산
    change = money - cup * 100
    # 커피 잔 수와 잔돈 전달하면서 prn 호출
    if change >= 0:
        prn(cup, change)
    else:
        prn()
    

def prn(cup=0, change=0):
    # 출력
    # 커피 X잔이 나왔습니다. 잔돈은 Y원 입니다. / 돈이 부족합니다.
    if cup == 0 & change == 0:
        print('돈이 부족합니다. 다시 입력해주세요.')    
        start()
    else:
        print('커피 {}잔이 나왔습니다. 잔돈은 {}원 입니다.'.format(cup, change))
    
    
def start():
    # 커피 잔 수 입력
    cup = int(input('몇 잔 뽑으실건가요 : '))
    # 돈 입력
    money = int(input('얼마를 넣으실건가요 : '))
    # coffee 함수에 잔 수와 돈 전달하면서 호출
    coffee(cup, money)

    
if __name__ == '__main__':
    start()
