import random

t = tuple(random.randint(1, 100) for i in range(10))
print(t)
# simple we reverse the tuple by built in function 
L = list(t)
# print(L)
# L.reverse()
# print(L.sort())
# L.sort(key=None, reverse=True)
L.reverse()
print(L)
L[0] = 1
print(tuple(L))
