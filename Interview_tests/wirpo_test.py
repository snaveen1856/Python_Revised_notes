my_lst = [2, 3, 11, 2, 3, 4, 3, 44, 3, 66, 0, 3]
sum_list = []
for i, s in enumerate(my_lst):
    if s == 3 and len(my_lst) > i + 1:
        # print(i, s)
        sum_list.append(my_lst[i + 1])

print(sum_list)
sum_num = sum(sum_list)
print(sum_num)
print('-'*40)
print("Using Generator logic:")
s_l = [my_lst[i+1] for i, e in enumerate(my_lst) if e==3 and len(my_lst) > i + 1]
print("Sum of list:", sum(s_l))
print("This is a generator list:", s_l)
print('-'*40)


def outer(func):
    def inner(*args, **kwargs):
        print('pre-operations of func')
        # result = func(*args, **kwargs)
        result = func()
        print('real operation', result)
        print('After operations of func')
        return result

    return inner


@outer
def add_nums(a=10, b=20):
    return a + b


print("function output:", add_nums())
