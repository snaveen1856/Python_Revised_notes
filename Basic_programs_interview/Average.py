# Average of entered numbers
import random

l = [random.randint(1, 10) for i in range(int(input('Enter how many terms you want get average:')))]
total = 0
count = len(l)
print(l)
for n in l:
    total += n
avg = (total / count)
# print(total // count)
print('Average:', round(avg, 2))
