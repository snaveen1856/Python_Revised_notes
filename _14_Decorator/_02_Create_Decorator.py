def outer(func_name):
    a = 10
    def inner(x, y):
        result = func_name()
        return result

    return inner


@outer
def add_nums(a, b):
    a, b = 10, 5
    return a + b


a = add_nums(50, 70)
print(a)
