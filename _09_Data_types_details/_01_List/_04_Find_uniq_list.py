import random
from itertools import count

n = [random.randint(1, 20) for i in range(10)]

print('List of n: ', n)
new_l = []
for i in n:
    if i not in new_l:
        new_l.append(i)
print('\nNew List unique values of n: ', new_l)
print('Length of new list: ', len(new_l))

'''
By using count() method we can find only count==1 items
'''
new_list = []
for i in n:
    if n.count(i) == 1:
        new_list.append(i)

print('\nUnique values of list using count method:', new_list)
''' 
same Functionality can achieved by convert list to set and again convert set to list
'''
