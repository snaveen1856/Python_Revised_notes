def my_deco(func):
    def wrapper(*args):
        print('we are in Decorator function before actual function execution')
        result = func(*args)
        return f"Hello! {result}"

    return wrapper


@my_deco
def print_name(string):
    return f'{string}'


name = input('enter name: ')
print(print_name(name))
