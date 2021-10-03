def sum_(num1: list, num2):
    print("-------", type(num1))
    result = num1 + num2
    print("result is ", result)
    return result


output = sum_(10, 20)
print(output)
print(sum_(10, 20))
print("Type of sum ", type(sum_), type(10))

# https://realpython.com/primer-on-python-decorators/

'''
Functions:
============
1. First Class functions
2. Nested Functions
3. Returning Functions
'''


def get_details(abc):
    return abc + 1


def sam(bar):
    print("Output is :", bar + 1)
    return bar + 1


# 1
sam(10)
# 2
print("Function call :", sam(10))
# 3
x = sam(10)
print("Assigned to x :", x)

op = get_details(sam(10))
print("Func call with function call as arg: ", op)

print(sam(2) == 3)  # functions return a value based on the given arguments.

# 1. FIRST CLASS FUNCTIONS:
print("----------1. FIRST CLASS FUNCTIONS------------")


def navn(bar):
    return bar + 1


navn(2)
print(navn(3))
print(type(navn(sam(10 + 20))))
print("Type of Navn :", type(navn))
print("Function Navn ", navn)

print("------------------------------------")

'''
Here Navn_func requires function name why because 
we have used the same parameter during function call
'''

# function call function_name(arguments)
'''
3 friends - A         B          c     -  1 + 1   
                                          1 - 1   
                                          1+  1    
                                          1   1+
'''


# 1.A
def john(bar):  # john(10)
    print("---------in john() function-----------")
    return bar + 1


print("--------------- john-------------------", john(2))
print("--------type of john-------------------", type(john))


# 2. B
def call_func_with_arg(john_func, val):
    print("---------in call_john_with_arg() function-----------")
    res = john_func(val)

    return res  # john("python")


print("Normal class function call:", john(100))
# 3. C
print("First class function call :", call_func_with_arg(john, 100))  # john(100) ==> john  100
print("------------------------------------")
