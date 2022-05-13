# Sum of all items in list
# 1.Using loops coding  2.Built-in function {<listname>.sum()} 

import random

l = [random.randint(1, 50) for i in range(10)]
print('List L = ', l)
sum_list = 0
for i in l:
    sum_list += i
    print(i, '+', end=' ')
print("\n Sum of List: ", sum_list)
# Using list Built-in Function Sum(l)

print("\n Sum of List Using Built-in Function: ", sum(l))
jkhjkkjj

