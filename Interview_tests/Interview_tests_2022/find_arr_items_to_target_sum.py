# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target. You may assume that each input would have exactly one solution, and you
# may not use the same element twice. You can return the answer in any order.

# Example1
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def target_sum(arr, t):
    temp = tuple(arr)
    if t in arr:
        return arr.index(t)
    res = []
    while arr:
        num = arr.pop()
        diff = t - num
        if diff in arr:
            res.append((num, diff))
    res_idx = [(temp.index(i[0]), temp.index(i[1])) for i in res]
    return res_idx


ar = [1, 5, 6, 7, 9, 8, 2, 3]
tar = 12
# ar = [2, 7, 11, 15]
# tar = 9
print(f'Given list:{ar} and target:{tar}')
print(target_sum(ar, tar))
