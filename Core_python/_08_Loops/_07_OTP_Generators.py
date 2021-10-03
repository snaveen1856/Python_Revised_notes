"""
OTP generate using random and  infinite loops
"""

import random

otp = 0
for i in range(6):
    otp = otp * 10 + random.randint(0, 9)
print('OTP: ', otp)
print('Good Bye')

pt = 0
pt = [str(pt * 10 + random.randint(0, 9)) for _ in range(6)]
print(pt)