"""
string function and method

s='this is a test string'
s.count('t')
s.count('is')
"""

text = input('Enter the text:')
char_count = {}
for char in text:
    if char not in char_count and char != ' ':
        char_count[char] = text.count(char)
print(char_count)
