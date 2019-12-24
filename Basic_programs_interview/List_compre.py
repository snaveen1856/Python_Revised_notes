# List comprehension function
import random

l = []
for i in range(10):
    l.append(random.randint(1, 50))
# l=[random.randint(1,50) for x in range(10)]
print(l)
sqr_list = [x ** 2 for x in l]
print(sqr_list)
