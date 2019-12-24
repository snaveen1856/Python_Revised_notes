# using lambda function/Anonymous function

l = list(range(1, 16))
even_l = list(filter(lambda x: x % 2 == 0, l))
print('l:', l)
print('Even list:', even_l)
