# # Python3 program to find all pairs in
# # a list of integers with given sum
#
# def findPairs(lst, K):
#     res = []
#     if K in lst:
#         res.append((K,))
#     while lst:
#         num = lst.pop()
#         diff = K - num
#         if diff in lst:
#             res.append((diff, num))
#     # res.reverse()
#     return res
#
#
# # Driver code
# lst = [1, 5, 3, 7, 9]
# numbers = [1, 2, 3, 7, 8, 7, 9, 20, 10]
# K = 10
# print(findPairs(numbers, K))
#
# # Python3 program to find all pairs in
# # a list of integers with given sum
#
# from itertools import combinations
#
#
# def findPairs(lst, K):
#     res = []
#     if K in lst:
#         res.append((K,))
#     for var in combinations(lst, 2):
#         if var[0] + var[1] == K:
#             res.append((var[0], var[1]))
#     for var in combinations(lst, 3):
#         if var[0] + var[1] + var[2] == K:
#             res.append((var[0], var[1], var[2]))
#     return res
#
#
# # Driver code
# l = [1, 2, 3, 7, 8, 7, 9, 20, 10]
# K = 10
# print(findPairs(l, K))


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


d = [1, 8, 5, 9, 2, 4, 7]
l = [1, 2, 3, 7, 8, 7, 9, 20, 10]
print(list(combinations(d, 4)))
print([i for i in list(combinations(l, 3)) if sum(i) == 10])
