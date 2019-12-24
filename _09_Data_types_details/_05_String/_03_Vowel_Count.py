"""
Program about count a vowel in string
"""
s = input('Enter a string:')
vowel_count = {}
vowel_char = ('a', 'e', 'i', 'o', 'u')
for i in s:
    if i in vowel_char:
        vowel_count[i] = s.count(i)

print(vowel_count)
