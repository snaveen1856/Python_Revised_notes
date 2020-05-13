import random


def unique_l(l):
    new_l = []
    for i in l:
        if l.count(i) == 1:
            new_l.append(i)
    print('New list unique of l:', new_l)


def check_uniq(l):
    new = []
    for i in l:
        if i not in new:
            new.append(i)
    return new


l = [random.randint(1, 50) for i in range(10)]
print('List l:', l)
unique_l(l)
print('Using function check num in list: ', check_uniq(l))
