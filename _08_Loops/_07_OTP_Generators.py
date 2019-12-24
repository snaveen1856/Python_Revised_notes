""" OTP generate using random and  infinate loops
"""
while True:
    import random

    otp = 0
    for i in range(6):
        otp = otp * 10 + random.randint(0, 9)
    print('OTP: ', otp)
    s = input('Do you want another OTP:[y/n]:')
    if s in ('n', 'N'):
        print('Good Bye')
        break
