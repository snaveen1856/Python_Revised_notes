"""
This Program will give the no of permutations and using list comprehension
we in maths npr
 """
L1 = [i for i in range(1, 5)]
L2 = [k for k in range(5, 9)]
print(L1)
print(L2)
all_perm = []
for a in L1:
    for b in L2:
        all_perm.append(a * b)
print('All permutation of L1&L2:', all_perm)
