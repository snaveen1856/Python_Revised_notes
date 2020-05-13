"""
import itertools

x = itertools.combinations(range(-3, 5), 3)
l = list(x)
print(l)
nl = []
for item in l:
    if sum(list(item)) == 0:
        nl.append(item)
print(nl[0])
"""
# dic = {"MON": 1, "TUE": 2, "WED": 3, "THR": 4, "FRI": 5, "SAT": 6, "SUN": 7}
# rev_dic = {1: "MON", 2: "TUE", 3: "WED", 4: "THR", 5: "FRI", 6: "SAT", 7: "SUN"}
#
# day = input("Enter a day:")
# num = int(input("Enter a number from you want:"))
# k = dic[day]
# i = (k + num) % 7
# print(i)
# print(f"From {day} after {num} number of days is: {rev_dic[i]}")
week = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
print(week)
day = input('Enter a day from above:')
num = int(input('Enter a number after how many days:'))
k = num + week.index(day)
k = k % 7
print(k)
print(week[k])

d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
s = int(input("Enter a number:"))
k = input("Enter a number in words in-between 5: ")
multi = s * d[k]
print(multi)

