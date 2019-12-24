# Returning more than one values in Function
def divmod(x, y):
    # a=x//y
    # b=x%y
    # return a,b
    return x // y, x % y


while True:
    n1 = int(input('Enter a number n1:'))
    n2 = int(input('Enter a number n2:'))
    r1, r2 = divmod(n1, n2)
    print(r1, r2)
    opt = input('Do you want once again division:[y/n]:')
    if opt in ('n', 'N'):
        break
