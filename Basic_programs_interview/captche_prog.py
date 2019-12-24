# captcha program
import random


def captcha(letters=6):
    l = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    s = ''
    for i in range(letters):
        s = s + random.choice(l)
    return s


c = captcha()
print('Captche of 6 char:', c)
c = captcha(4)
print('Captche of 4 char:', c)
