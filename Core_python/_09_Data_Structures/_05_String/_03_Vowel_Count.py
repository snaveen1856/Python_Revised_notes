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

# Test of Nithin
# s = input('Enter a string:')
# vowel_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
# vowel_char = ('a', 'e', 'i', 'o', 'u')
# rem_str = ''
# for i in s:
#     if i in vowel_char:
#         vowel_count[i] = s.count(i)
#     else:
#         rem_str += i
# print(vowel_count)
# print(rem_str)
