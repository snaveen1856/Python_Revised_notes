# Function def. and syntax
def add(x, y):
    """It receive two argument and returns addition"""
    return x + y


print(add(24, 8))
print(add(1.8, 5.6))
print(add('hello', 'world'))
print(add([1, 2, 3], [4, 5, 6]))
print(add.__doc__)
print(add.__dir__())
