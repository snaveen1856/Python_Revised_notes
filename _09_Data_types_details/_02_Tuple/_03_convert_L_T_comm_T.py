import random
from itertools import count

t = tuple()
t1 = tuple(random.randint(1, 50) for i in range(10))
print("t1=", t1)
s = []
for i in range(5):
    a = int(input('Enter a number:'))
    s.append(a)
t = tuple(s)
for j in t:
    if count(j) == 1:
        pass
    else:
        print(j)
