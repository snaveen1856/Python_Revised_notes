def my_deco(func):
    def wrapper(args, *kwargs):
        print('before func call: ')
        args = list(ar * 2 for ar in args)
        res = func(args, *kwargs)
        print('args: ', args)
        print('kwargs: ', kwargs)
        print('after func call: ', res * 2)
        return res

    return wrapper


@my_deco
def f1(args, *kwargs):
    return args, kwargs
