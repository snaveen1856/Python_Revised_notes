# 1. MergeSort
# ---------------

def mergeList(l1, l2):
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
    return res


def mergeSort(l):
    if len(l) < 2:
        return l
    mid = len(l) / 2
    first = mergeSort(l[mid:])
    last = mergeSort(l[:mid])
    return mergeList(first, last)

# 2. QuickSort
# ------------

def quickSort(l):
    if not l:
        return []
    else:
        pivot = l[0]
        less = [x for x in l if x < pivot]
        greater = [x for x in l[1:] if x >= pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


# 3. HeapSort
# ------------

import heapq


def heapSort(l):
    h = l[:]
    heapq.heapify(h)
    res = [heapq.heappop(h) for _ in range(len(h))]
    return res