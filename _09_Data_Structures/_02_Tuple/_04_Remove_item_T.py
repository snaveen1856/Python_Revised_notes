import random

t = tuple(random.randint(1, 50) for i in range(10))
print(t)
L = list(t)
for i in t:
    if t.count(i) == 1:
        print(i, end=' ')
while True:
    n = int(input('\nEnter a number in the tuple to remove:'))
    L.remove(n)
    opt = input('Do you want remove number in tuple [y:n]:')
    if opt in ('n', 'N'):
        break
t = tuple(L)
print(t)
