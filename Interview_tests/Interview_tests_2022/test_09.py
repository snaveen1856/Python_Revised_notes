# 10010100001100

# select * from emp out where (select count(*) from emp inn where out.empno = inn.empno) > 1;

test_data = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.123.900
123*555*1234
800-555-1234
900-555-1234
200*784*3662
cat 
bat
mat
pat
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
import re

pattern = re.compile(r'\d\d[\d].\d\d[\d].\d[\d\d].\d[\d\d]')
#
# pattern = re.compile('[\d].[\d].[\d].[\d]')


# with open(test_data, '+r') as f_data:
#     # while f_data:
#     f_data.read()
#     contents = f_data.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# contents = f_data.read()
matches = pattern.finditer(test_data)
for match in matches:
    print(match)

import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)