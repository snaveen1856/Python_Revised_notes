import random


def even_l(l):
    for i in l:
        if i % 2 == 0:
            print(i, end=' ')


k = [random.randint(1, 50) for i in range(15)]
print('List k:', k)
even_l(k)
