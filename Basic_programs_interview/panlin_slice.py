# for loop sequence
# s="python"
# for ch in s:
# print(ch)
# print('done')

# for loop range

for i in range(10):
    print(i)

s = input("Enter a word:")
rev_s = s[::-1]
if rev_s == s:
    print('it is a Palindrome:')
else:
    print('its not a Palindrome:')
