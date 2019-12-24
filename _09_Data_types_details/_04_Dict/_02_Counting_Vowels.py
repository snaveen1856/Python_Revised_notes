# count char only of AEIOU in given string

text = input('Enter a text:')
char_count = {}
vowel = 'aeiou'
for char in vowel:
    char_count[char] = text.count(char)  # Here inserting a key value pair in dict using count()
print(char_count)
