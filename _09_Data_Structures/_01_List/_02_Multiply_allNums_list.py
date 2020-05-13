# Multiplying the all items in the list
import random

l = [random.randint(1, 20) for i in range(4)]
print('List l= ', l)
m = 1
for i in l:
    m *= i
print('Multiplying of all items in the list: ', sum(l))

print()
