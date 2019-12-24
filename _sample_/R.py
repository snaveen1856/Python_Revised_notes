l = [1, 'a', 2, 9, 8]
try:
    for i in range(len(l)):
        print(l[i])
    k = int(input('Enter a number:'))
except:
    if k <= len(l):
        print(l[k])
        print('Congrats')
    else:
        print('Try again')
