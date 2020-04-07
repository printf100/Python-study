# -*- coding:utf-8 -*-

# 로또
import random

lotto = list()

for i in range(0, 6):
    r1 = random.randint(1, 45)
    lotto.append(r1)
    
    if(lotto[i] == r1):
        continue
    else:
        lotto.append(r1)

lotto.sort()
print(lotto)


def lotto():
    lotto = set()
    
    while len(lotto) < 6:
        ran = random.randint(1, 45)
        lotto.add(ran)
    # print(list(lotto))
    lst = sorted(lotto)
    print(lst)
    

if __name__ == '__main__':
    lotto()
