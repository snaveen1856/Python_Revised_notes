import random

# n = int(input('Enter a number:'))
n = random.randint(-10000, 10000)
print('Enter number:', n)
l = [i for i in range(n)]
print('Given list:', l)
a = sum(l)
print('Sum of list:', a)
if a % 2 == 0:
    a1 = a / 2
    if n % 2 != 0 and n > 0:
        l.remove(0)
    l1 = []
    print('Half of the sum of list:', a1)
    j = -1
    i = 0
    while i < n//2:
        l1.append(l[i])
        l1.append(l[j])
        i += 1
        j -= 1
        l1.append(-l[i])
        l1.append(-l[j])
        i += 1
        j -= 1
    #print(l1)
    if n % 2 != 0 and n > 0:
        l1.append(0)
    else:
        l1 = l1
    l1.sort()
    print('Required New list:', l1)
    print('sum of new list:', sum(l1))
    print('Length of New list:', len(l1))

else:
    print('we can not make list for this number!')


