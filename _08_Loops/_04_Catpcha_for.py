# captcha program
import random


def captcha(letters=6):
    l = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*&%$#@!')
    s = ''
    for i in range(letters):
        s = s + random.choice(l)
    return s


c = captcha()
print('Captcha with 6 character:', c)
c = captcha(4)
print('Captcha with 4 character:', c)
