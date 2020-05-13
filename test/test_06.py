"""
import time

start = time.perf_counter()


def do_something():
    print("Sleeping 1 second ")
    time.sleep(1)
    print("Done sleeping")


do_something()
do_something()
do_something()
do_something()
do_something()
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")
"""
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
d = list(zip(l2, l1))
dt = {}
print(d)
for i in range(len(l1)):
    dt[l2[i]] = l1[i]
print("Dt =", dt)

s = {k: v for k, v in d}
print('s =', s)

a = 'i am naveen'
a1 = a.split(' ')
print('a1 =', a1)
print('a1 =', a[::-1])



