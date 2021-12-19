# l = [1, 'a', 2, 9, 8]
# try:
#     for i in range(len(l)):
#         print(l[i])
#     k = int(input('Enter a number:'))
# except:
#     if k <= len(l):
#         print(l[k])
#         print('Congrats')
#     else:
#         print('Try again')

from datetime import *

c = ''
s = datetime.strptime('22:30', '%H:%M')
print(s.strftime('%r'))
