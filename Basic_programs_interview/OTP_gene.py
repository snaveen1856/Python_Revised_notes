# OTP generate using random
import random

while True:

    otp = 0
    for i in range(6):
        otp = otp * 10 + random.randint(0, 9)
    print('OTP: ', otp)
    s = input('Do you want another OTP:[y/n]:')
    if s in ('n', 'N'):
        break
