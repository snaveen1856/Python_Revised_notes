import random

comm_a_b = []
diff_a_b = []
i1 = [random.randint(1, 50) for i in range(10)]
i2 = [random.randint(1, 50) for i in range(10)]
print('List i1:', i1)
print('List i2:', i2)
comm_a_b = [j for j in i1 for k in i2 if j == k]
print('Common B/W i1-i2=', comm_a_b)
k = 0
for j in i1:
    k = j
    for k in i2:
        s = k - j
        diff_a_b.append(s)
        break
    continue

print(diff_a_b)

'''
for i in i1:
    s=i1.index(i)
    print(s,end=' ')
    
 '''
