def str_(str1):
    str2 = str1[::-1]
    if str2 == str1:
        # pass
        print('It is palindrome!')
    else:
        # pass
        print('It is not palindrome!')
    res_str = ''
    for i in str1:
        res_str = i + res_str
    if str1 == res_str:
        print('palindrome')
    else:
        print('Not a palindrome')


string = input('Enter a string:')
str_(string)
# print(f'{str1} is a ', str_(str1))
