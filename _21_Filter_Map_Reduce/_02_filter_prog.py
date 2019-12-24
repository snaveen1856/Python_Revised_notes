import random


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


# sequence
# sequence = str(input('Enter a sequence of char"s:'))
sequence = str(input('Enter a sequence of char"s:'))
# using filter function 
filtered = list(filter(fun, sequence))
s = ''
for i in filtered:
    s += i
print(s)
print(type(s))
print('The filtered letters are:', filtered)
