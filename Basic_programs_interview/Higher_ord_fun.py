# High ordered function .i.e., function in function
def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def math_op(x, y, task):
    return task(x, y)


s = math_op(18, 56, add)
print(s)
n = math_op(12, 13, mult)
print(n)
