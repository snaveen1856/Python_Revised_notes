"""
def mergelist(l1, l2):
    i = j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    res.extend(l1[i:])
    res.extend(l2[j:])
    # print(res)
    return res


def mergesort(l):
    if len(l) < 2:
        return l
    mid = len(l) // 2
    fi = mergesort(l[mid:])
    la = mergesort(l[:mid])
    return mergelist(fi, la)


given_l = [33, 20, 1, 4, 55, 6, 65, 7, 76]
req = mergesort(given_l)
print(req)

"""

"""
def quicksort(l):
    if not l:
        return []
    pivot = l[0]
    less = [x for x in l if x < pivot]
    greater = [x for x in l[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


g_list = [34, 23, 45, 66, 65, 7, 76, 68, 33, 5, 3]
result = (quicksort)(g_list)
print(result)
"""

import heapq


def heapsort(l):
    h = l[:]
    heapq.heapify(h)
    res = [heapq.heappop(h) for _ in range(len(h))]
    return res


g = [2, 56, 89, 6, 34, 74, 1, 53]
result_l = heapsort(g)
print(result_l)
