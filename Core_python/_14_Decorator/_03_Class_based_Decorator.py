# Python program showing
# class decorator with
# return statement

class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # before function
        result = self.function(*args, **kwargs)

        # after function
        return result

    # adding decorator to the class


@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n


print("Square of number is:", get_square(195))

print('=============================================================')


class MyClassDecorator:
    def __init__(self, *a, **kw):
        self.conf_args = a
        self.conf_kw = kw
        # self.func  = None

    def __call__(self, func):
        # self.func = func
        def wrapper(*args, **kwargs):
            print('pre-processing')
            print('pre-processing configuration', self.conf_args, self.conf_kw)
            if args:
                if isinstance(args[0], int):
                    a = list(args)
                    a[0] += 5
                    args = tuple(a)
                    print('pre-process OK', args)
            r = func(*args, **kwargs)
            print('postprocessing', r)
            r += 7
            return r

        return wrapper


@MyClassDecorator(1001, a='some configuration')
def my_function(*args, **kwargs):
    print('call my_function', args, kwargs)
    return 3


my_function(1, 2, 3, a="OK")

"""
output:
=======
In [1]: my_function(1,2,3, a="OK")

preprocessing
preprocessing configuration (1001,) {'a': 'some configuration'}
preprocess OK (6, 2, 3)
call my_function (6, 2, 3) {'a': 'OK'}
postprocessing 3
Out[1]: 10
"""
