def math_sum(l):
    sum_ = 0
    for i in l:
        sum_ += i
    return sum_


s = [1, 2, 3, 4, 5]
print('Sum of list is', math_sum(s))
print(__name__)
