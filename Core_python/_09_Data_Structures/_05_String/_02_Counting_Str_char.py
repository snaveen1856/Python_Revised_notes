"""
string function and method

s='this is a test string'
s.count('t')
s.count('is')"""

text = input('Enter the text:')
char_count = 0
for char in text:
    if char != ' ':
        char_count = char_count
    char_count += 1
print('Number of Characters in Text string:', char_count)
