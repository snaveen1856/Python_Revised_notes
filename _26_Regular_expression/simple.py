import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
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
sentence = 'Start a sentence and then bring it to an end'
"""
pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
print(matches)
"""
# pattern = re.compile(r'123')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms.com')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'[892]00[-.*]\d\d\d[-.*]\d\d\d\d')
pattern = re.compile(r'[^b]at')
with open('Data.txt') as fl:
    contents = fl.read()
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
