import random

s = [random.randint(1, 100) for i in range(6)]
print('List s=', s)
l = []
for i in s:
    l.append(i)

print('Copy of list s is l=', l)
''' 
same functionality can achieved by copy() method
'''
print('Copy of list s using copy method =', s.copy())
