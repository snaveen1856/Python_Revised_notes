# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
# def solution(A):
#     # write your code in Python 3.6
#     shift = 0
#     size = len(A)
#     for i in range(size):
#         if (A[i] <= 0):
#             A[i],A[shift] = A[shift],A[i]
#             shift +=1
#     res, req_size = A[shift:], (size - shift)
#     for idx in range(req_size):
#         if (abs(res[idx]) -1 < req_size) and A[abs(res[idx]) - 1] > 0:
#             res[abs(res[idx]) - 1] = -res[abs(res[idx]) - 1]
#     num = 0
#     for i in range(req_size):
#         if (res[i] > 0):
#             num = i + 1
#         num = size + 1
#     return num
#
# a = [0,10,2,-10,-20]
#
# res = solution(a)
# print(res)
# ============================================================
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
# def solution(A, K):
#     # write your code in Python 3.6
#     N = len(A)
#     if K > N:
#         return -1
#     max_sum, even, odd = 0, [], []
#     # for i in range(N):
#     #     if A[i] % 2:
#     #         odd.append(A[i])
#     #     else:
#     #         even.append(A[i])
#     even = [i for i in range(N) if A[i] % 2]
#     odd = [i for i in range(N) if A[i] not in A]
#     odd.sort(reverse=False)
#     even.sort(reverse=False)
#     even_len = len(even) - 1
#     odd_len = len(odd) - 1
#     while K > 0:
#         if (K % 2) == 1:
#             if even_len >= 0:
#                 max_sum += even[even_len]
#                 even_len -= 1
#             else:
#                 return -1
#             K -= 1
#         elif even_len >= 1 and odd_len >= 1:
#             if even[even_len]+even[even_len - 1] <= odd[odd_len] + odd[odd_len - 1]:
#                 max_sum += odd[odd_len] + odd[odd_len - 1]
#                 odd_len -= 2
#             else:
#                 max_sum += even[even_len] + even[even_len - 1]
#                 even_len -= 2
#             K -= 2
#         elif even_len >= 1:
#             max_sum += even[even_len] + even[even_len - 1]
#             even_len -= 2
#             K -= 2
#         elif odd_len >= 1:
#             max_sum += odd[odd_len] + odd[odd_len - 1]
#             odd_len -= 2
#             K -= 2
#     return max_sum
#
# a = [2,4,10,3,5]
# k = 3
# print(solution(a,k))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A):
    # write your code in Python 3.6
    table_01 = {}
    location_count = 0
    for loc in A:
        if A[loc] not in table_01:
            location_count += 1
    idx1 = 0
    day_count = max(A)
    table_02 = {}
    while idx1 < len(A):
        idx2 = idx1
        prev_day = idx2
        res = 0
        count_01 = 0
        while idx2 < len(A):
            if A[idx2] not in table_02:
                count_01 += 1
                res += idx2 - prev_day
                table_02[A[idx2]] = table_02[A[idx2]] + 1
            idx2 += 1
        if count_01 == location_count:
            day_count = min(res, day_count)
        table_02.clear()
        idx1 += 1
    return day_count + 1


from collections import Counter


def solution1(A):
    res = {val: 1 for val in set(A)}
    missing_num = len(res)
    cur_i = result_i = result_j = 0
    for cur_j, num in enumerate(A, 1):
        if res[num] > 0:
            missing_num -= 1
        res[num] -= 1
        if not missing_num:
            while cur_i < cur_j and res[A[cur_i]] < 0:
                res[A[cur_i]] += 1
                cur_i += 1
            if not result_j or cur_j - cur_i <= result_j - result_i:
                result_i, result_j = cur_i, cur_j
    return result_j - result_i


a = [2, 1, 1, 3, 2, 1, 1, 3]
b = [7, 5, 2, 7, 2, 7, 4, 7]
c = [7, 3, 7, 3, 1, 3, 4, 1]
print(solution1(a))
