# import array as ar
from array import *

a = array('i', [1, 2, 3, 5, 8, 9, 6])
a.append(10)
b = array('i', [7, 3, 8, 10])
a.extend(b)
print(a.buffer_info())
print(b.byteswap())
for e in a:
    print(e)
