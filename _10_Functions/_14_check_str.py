def check_str(s):
    char_count = {}
    for char in s:
        if char not in char_count and char != ' ':
            char_count[char] = s.count(char)
    print(char_count)


def check_U_L(s):
    str = list(s)
    upper_l = 0
    lower_l = 0
    ul = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ll = list('abcdefghijklmnopqrstuvwxyz')
    for i in str:
        if i in ul:
            upper_l += 1
        else:
            lower_l += 1
    return upper_l, lower_l


str = input('Enter a text: ')
check_str(str)
print('upper letter,lower letter:', check_U_L(str))
