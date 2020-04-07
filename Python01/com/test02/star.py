# -*- coding:utf-8 -*-

'''
*
**
***
****
*****
'''
    
for i in range(1, 6):
    print('*' * i)
print()

print('\n'.join([' '.join(['*' for i in range(i+1)]) for i in range(5)]))
print()

'''
*****
****
***
**
*
'''

for i in range(5, 0, -1):
    print('*' * i)
print()


'''
    *
   **
  ***
 ****
*****
'''

cnt01 = 4
for i in range(1, 6):
    print(' ' * cnt01, '*' * i)
    cnt01 -= 1
print()

'''
*****
 ****
  ***
   **
    *
'''

cnt02 = 5
for i in range(0, int(cnt02)):
    print(' ' * i, '*' * cnt02)
    cnt02 -= 1
print()

'''
    *
   ***
  *****
 *******
*********
'''

cnt03 = 4    
for i in range(1, 10, 2):
    print(' ' * cnt03, '*' * i)
    cnt03 -= 1

