# Palindrome with different logic
string = input('Enter a text string:')
length = len(string)
rev_string = ''
for i in range(-1, (-length - 1), -1):
    substring = string[i]
    rev_string += substring
if rev_string == string:
    print('Entered string is a Palindrome!')
else:
    print('Entered string is not a Palindrome!')
print('----------------------------------------------')


word = input('Enter a word:')
for each in range(0, len(word) // 2):
    if word[each] != word[len(word) - each - 1]:
        print('Entered string is not a Palindrome!')
    else:
        print('Entered string is a Palindrome!')

print('----------------------------------------------')


# function to check string is
# palindrome or not
def isPalindrome(string1):
    # Run loop from 0 to len/2
    for i in range(0, len(string1) // 2):
        if str[i] != str[len(string1) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Palindrome")
else:
    print("Not a Palindrome")
print('-------------------------------------------------')

# Python program to check
# if a string is palindrome
# or not

x = "malayalam"
w = ""
for i in x:
    w = i + w
if x == w:
    print("Palindrome")
else:
    print('Not a Palindrome')