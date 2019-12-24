""" This program contains How to unpack the tuple,concadinate the two tuples,
    converting tuple to string and using random package and range built-in functions
    creating tuple.

"""
import random

t1 = tuple(random.randint(1, 50) for i in range(10))
t2 = tuple(random.randint(1, 50) for i in range(10))
print(t1, end=' ')
l = []
for j in 'abcdefghij':
    print(j, end=' ')
    l.append(j)

a, b, c, d, e, f, g, h, i, j = tuple(random.randint(1, 50) for i in range(10))
print('\n', a, b, c, d, e, f, g, h, i, j)
print(t1 + t2)
s = ''
for i in t1:
    a = str(i)
    s += a
print(s)
