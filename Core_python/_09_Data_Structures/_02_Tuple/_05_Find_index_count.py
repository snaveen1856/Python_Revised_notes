import random

t = tuple(random.randint(1, 50) for i in range(10))
print(t)
L = list(t)
print(L)
print('Number only occur once in tuple:')
for i in t:
    if t.count(i) == 1:
        print(i, end=' ')

while True:
    i = int(input('\nEnter a number to find index and count:'))
    print('Index of the number:', i, ':', t.index(i))
    print('Count of the number:', i, ':', t.count(i))
    opt = input('Do you want to find another number[y/n]:')
    if opt in ('N', 'n'):
        print('done')
        break
