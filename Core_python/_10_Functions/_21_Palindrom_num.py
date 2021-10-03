def palindrome_num(n):
    tru = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if rev == tru:
        print('Given number is Palindrome!')
    else:
        print('Given number is not Palindrome!')


def sum_digits(k):
    s = 0
    while k > 0:
        dig = k % 10
        s += dig
        k = k // 10
    return s


n = int(input('Enter a number: '))
palindrome_num(n)
print('Sum of Digits are:', sum_digits(n))
