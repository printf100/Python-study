# -*- coding:utf-8 -*-


def factorial(n):
    f = 1
    
    for n in range(n, 0, -1):
        f *= n
    
    return f


fr = 1


def factorialRecursion(n):
    global fr
    
    if n == 0:
        return fr

    fr *= n
    
    return factorialRecursion(n - 1)

# def factorialRecursion(n):
#     if n == 1:
#         return 1
#     
#     return n * factorialRecursion(n - 1)


if __name__ == '__main__':
    n = int(input('n : '))
    res = factorialRecursion(n)
    print('{} factorial = {}'.format(n, res))
    print('{} factorial = {}'.format(n, factorial(n)))    
