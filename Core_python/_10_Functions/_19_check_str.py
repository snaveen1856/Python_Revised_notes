def check_pangram(str):
    l = ['abcdefghijklmnopqrstuvwxyz']
    for i in str:
        for k in l:
            if k == i:
                print('It is a pangram!')
    else:
        print('It is not a pangram!')


string = input('Enter a string: ')
check_pangram(string)
