# maximum of 3 numbers

a = int(input('Enter a value:'))
b = int(input('Enter b value:'))
c = int(input('Enter c value:'))
if a > b:
    m = a
else:
    m = b
if c > m:
    m = c
print('Max: ', m)
