# -*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']

for i in subject:
    print(i)
    
    
for i in subject:
    print(i, end=' ')   # 끝에 공백을 붙여줌 (default는 \n)
else:   # python의 모든 제어문에는 else를 붙여줄 수 있음!
    print('\n재밌다')  # 반복문이 정상 종료되었을 때 수행됨
    
    
for i in range(1, 100):
    print(i, end=', ')
else:
    print(100)
    
print('------------------------------')

# 구구단
print('[ 구구단 ]')
for i in range(2, 10):
    print('\n< '+str(i)+'단 >')
    for j in range(1, 10):
        print(i, 'X', j, '=', i*j, sep=' ')     # sep : 중간 중간 공백을 넣어줌
print()
        
# 10부터 거꾸로
for i in range(10, 0, -1):
    print(i)
    
    