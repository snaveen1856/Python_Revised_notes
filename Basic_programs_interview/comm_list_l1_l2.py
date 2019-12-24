# print a list have common items in both lists i.e., n1,n2
import random


def comm_l(l1, l2):
    l = []
    for i in l1:
        for k in l2:
            if i == k:
                l.append(k)
    return l


k1 = []
for i in range(10):
    k1.append(random.randint(1, 20))
print('List of K1 =:', k1)
k2 = []
for k in range(10):
    k2.append(random.randint(1, 20))
print('List of K2 =', k2)
s = []
s = comm_l(k1, k2)
print('Common list of k1and k2=>S =', s)
