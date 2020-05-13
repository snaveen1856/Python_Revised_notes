"""
Create a mapping function and filter function
"""
import random
from _functools import reduce


def is_even(n):
    return n % 2 == 0


def update_list(n):
    return n * 2


def sum_all(a, b):
    return a + b


l = [random.randint(1, 50) for i in range(10)]
evens = list(filter(lambda n: n % 2 == 0, l))
doubles = list(map(lambda a: a * 2, evens))
add_all = reduce(lambda a, b: a + b, doubles)

# evens = list(filter(is_even,l))
# doubles = list(map(update_list,evens))
# add_all = reduce(sum_all,doubles)

print('List l=', l)
print("Even number list=", evens, '\n', 'length of evens list=', len(evens))
print("double the number list=", doubles, '\n', 'length of evens list=', len(doubles))
print("sum of the number list=", add_all)
