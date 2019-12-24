import random
from random import randint


def sum_l(l):
    s = 0
    for i in l:
        s += i
    print("Sum of items in list: ", s)


k = []
k1 = [random.randint(1, 30) for i in range(10)]
for i in range(1, 11):
    k.append(random.randint(1, 30))
print('List k: ', k)
sum_l(k)
print('-----------------------')
print('List k1:', k1)
sum_l(k1)
