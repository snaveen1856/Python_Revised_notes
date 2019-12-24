import random


def is_even(num_list):
    if isinstance(num_list, list):
        new_even = []
        for num in num_list:
            if num % 2 == 0:
                new_even.append(num)
    return new_even


list_1 = [random.randint(1, 50) for i in range(10)]
print('Given list:', list_1)
print("Even number list:", is_even(list_1))
print("Using map and lambda functions:", list(filter(lambda n: n % 2 == 0, list_1)))
print('map function', list(map(lambda x: x ** 2, list_1)))
# l = 10
# print("Even number list:", is_even(l))
# try:
#     print("Even number list:", is_even(l))
# except Exception as er:
#     print(er)
# finally:
#     print('Done')
