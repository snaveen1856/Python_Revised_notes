import random


class Only_list(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def is_even(num_list):
    try:
        new_even = []
        if isinstance(num_list, list):
            for num in num_list:
                if num % 2 == 0:
                    new_even.append(num)
            # print('Even number in list:', new_even)
        else:
            raise Only_list('This function allows only list!')
    except Exception as e:
        print(e)
    finally:
        return new_even


list_1 = [random.randint(1, 50) for i in range(10)]
print('Given list:', list_1)
print("Even number list:", is_even(list_1))
l = 10
print("Even number list:", is_even(l))
try:
    print("Even number list:", is_even(l))
except Exception as er:
    print(er)
finally:
    print('Done')
