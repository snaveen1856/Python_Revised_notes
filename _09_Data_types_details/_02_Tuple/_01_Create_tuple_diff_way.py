"""
This code is to creating tuple in different ways.
"""
import random

t1 = tuple(i for i in range(11))
t2 = tuple(random.randint(1, 50) for i in range(10))
l = [random.randint(1, 50) for j in range(10)]
t3 = tuple(i for i in l)
t4 = tuple(l)
s = []
t6 = tuple()
t7 = (1, 2, 3, 4, 5, 6)
print(t7[2])
print(len(t7))
for j in range(3):
    a = input('Enter any thing:')
    s.append(a)
t5 = tuple(s)

print('Tuple t1=', t1)
print('Tuple t2=', t2)
print('\nList l=', l)
print('\nTuple t3=', t3)
print('Tuple t4=', t4)
print('Tuple t5=', t5)
print('Tuple t7:', t7)
