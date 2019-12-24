# Rolling a dice game

import random

a = random.randint(1, 6)
print('system rolled number: ', a)
otp = input('you want roll a dice:[y/n]:')
if otp in ('y', 'Y'):
    b = random.randint(1, 6)
    print('you rolled number: ', b)
if a > b:
    print('system won the game')
elif a < b:
    print('You won the game')
else:
    print('game is tie')
