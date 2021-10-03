def check_num(n):
    l = [i for i in range(1, 100)]
    if n in l:
        print('entered number is in given range!')
    else:
        print('entered number is not in given range!')


def test_range(n):
    if n in range(1, 50):
        print('Given number is in range!')
    else:
        print('Given number is not in range!  ')


k = int(input('Enter a number to check: '))
check_num(k)
test_range(k)
print(test_range(289))

