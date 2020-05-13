"""
t = 1,2,3,5,6,
print(t[3])
print(t)
a = sum(t)
t1 = list(t)
t1.insert(0,a)
print(tuple(t1))
"""
# l = [(1, 2, 3), (5, 3, 3), (4, 8, 8), (7, 3, 9)]
# l1 = []
# for i in l:
#     a = sum(i)
#     i1 = list(i)
#     i1.insert(0, a)
#     l1.append(tuple(i1))

# l1.sort()
# print(l1)
# l2 = [list(i) for i in l]
#
# print(sorted(l, key=lambda x: x[0] + x[1] + x[2]))
"""
l = [(1, 2, 3), (5, 3, 3), (4, 8, 8), (7, 3, 9)]
l1 = []
l2 = []
for i in l:
    i1 = list(i)
    i1.insert(0, sum(i))
    l1.append(i1)
l1.sort()
for j in l1:
    t = list(j)
    t.remove(t[0])
    t = tuple(t)
    l2.append(t)

print(l2)
l.sort(key=lambda x: x[0] + x[1] + x[2])

print(l)
print(sorted(l, key=lambda x: x[0] + x[1] + x[2]))
"""
# from datetime import date
#
#
# def cal_age(birthdate):
#     today = date.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age
#
#
# print(cal_age(date(1994, 9, 1)), "years")

from datetime import datetime, date, time, timedelta

# from datetime import timedelta

today = datetime.today()
yesterday = today - timedelta(days=20)

print(today)
print()
print(yesterday)

tf = time(12, 34, 45, 67)
print('tf:', tf)
t = datetime(2020, 3, 20, 12, 45, 50)
print('t:', t)
tod = date.today()
print('todaysLLL:', tod)
# t = date(2020, 2, 10)
# pr = t.toordinal()
# ne = date(2020, 3, 10)
# ne = ne.toordinal()
# s = ne + pr
# print(s, date.fromordinal(s))
f = timedelta(days=2, hours=4, seconds=46, minutes=38)
rf = today - f
print(rf)
