"""
http://pymbook.readthedocs.io/en/latest/igd.html

Decorator is way to dynamically add some new behavior to some objects.

"""
import functools

list1 = [1, 2, 3, 4, 5]


def my_decorator(func):
    print("-----Started executing the Decorator---------")

    def wrapper(*args, **kwargs):
        print("****  Before method call : Perform some pre action ****")
        result = func(*args, **kwargs)  # add(10, 20)
        print("****   After method call : Perform some post action ****")
        return result

    print("-----Stopping executing the Decorator---------")
    return wrapper


'''
Part1 : function_name   ===> func  :::  add
Part2 : function_args   ===> *args :::  10,20
Part3 : Python will load respective decorator by passing method name as argument and starts executing it
Part4 : PI will receive the nested function complete address(function name)
Part5 : It will execute nested function by passing the arguments which were received in step2
        wrapper(10,20)
Part6 : Nested function(here wrapper()) will be executed and returns the result if any to PI
Part7 : PI will pass the same result to our code  

What is decorator
Purpose of decorator.Advatanges Disadvantages
Python Decorators 
Django Decorators
Did you write any customized decorator
What is the decorator execution sequence if multiple decorators exists
'''


@my_decorator
def add(a, b):
    """Our add function"""
    print("----In add method-----")
    return a + b


@my_decorator
def fund_transfer(acno, name, amount):
    pass


print(add(10, 20))


def sub(a, b):
    print("----In subtract method-----")
    return a - b


add(1, 3)
sub(1, 3)
'''
Step 1 : First class function : my_decorator function will be called and executed by receiving our method
                                name as argument.  
Step 2 : Nested function      : In my_decorator function,nested will be there which will receive our method 
                                arguments.
Step 3:  Returning function  : wrapper function(i.e. nested function)  name will be returned

wrapper(a,b)
'''

print("-------DECORATOR 2------------")


def my_dec(func):
    @functools.wraps(func)
    def wrapper():
        print("Before decorator")
        func()
        print("After decorator")

    return wrapper()


@my_dec
def func():
    print("I am function")


print(func)

print("-------DECORATOR WITH ARGS---------")


def my_dec_arg(number):
    def my_dec_func(func):
        @functools.wraps(func)
        def wrapper_arg(*args, **kwargs):
            print("Before decorator")
            if number == 5:
                print("Not running function")
                print("DEC NO is :", number)
            else:
                func(*args, **kwargs)
            print("after decorator")

        return wrapper_arg

    return my_dec_func


@my_dec_arg(10)
def func_arg(x, y):
    print("Arguments passed")
    print(x + y)


func_arg(10, 20)
