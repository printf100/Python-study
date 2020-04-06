# -*- coding:utf-8 -*-

n = input('n 입력 : ')
print(n)

cnt = 2
a, b = 0, 1
fibo = [a, b]

while cnt < int(n):
    fibo.append(fibo[cnt-2] + fibo[cnt-1])
    cnt += 1
else:
    print(fibo)
    

i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a + b
    i += 1
print()