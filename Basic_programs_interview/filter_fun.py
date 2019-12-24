# function using FILTER
import random


def iseven(n):
    return n % 2 == 0


a = []
l = list(range(1, 11))
for i in range(11):
    a.append(random.randint(1, 50))
#  a[random.randint(0, 50) for i in range(10)]
print('a:', a)
print('l:', l)
even_a = list(filter(iseven, a))
even_l = list(filter(iseven, l))
print('EVEN LIST l:', even_l)
print('EVEN LIST a:', even_a)
print('Length of Even_l:', len(even_l))
print('Length of Even_a:', len(even_a))
print(type(frozenset(range(5))))
