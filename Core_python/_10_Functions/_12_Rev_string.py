def rev_str(s):
    l = []
    for i in s:
        l.append(i)
    # print(l)
    new_l = [char for char in s]
    print('Reverse the string using the method .reverse(): ', l.reverse())
    print('Reverse the string using the method .reverse(): ', new_l.reverse())


def rev_s(str1):
    revStr = ''
    index = len(str1)
    while index > 0:
        revStr += str1[index - 1]
        index = index - 1
    return revStr


string = input('Enter a string: ')
rev = string[::-1]
print('Reverse the string using slice operator: ', rev)
s = rev_s(string)
print('Reverse the string using function: ', s)
print('---------------------------------------------')
rev_str(string)