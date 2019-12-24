# using functions obtaining the max,min of List
import random


def min_max(l):
    if l:
        return min(l), max(l)
    return None, None


n = []
for i in range(10):
    n.append(random.randint(1, 100))
m1, m2 = min_max(n)
print('List of n:', n)
print('Min of list n: ', m1, '\nMax of list n: ', m2)
n1 = []
m1, m2 = min_max(n1)
print('List of n1:', n1)
print('Min of list n1: ', m1, '\nMax of list n1: ', m2)
