# Returning two values function
def abs_values(x):
    if x < 0:
        return -x
    return x


n = float(input('Enter a number:'))
a = abs_values(n)
print(a)
print(abs_values(-18.56))
print(abs_values(1856))
