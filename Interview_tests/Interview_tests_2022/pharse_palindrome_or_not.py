# Python program to find if a sentence is palindrome
# To check sentence is palindrome or not
def sentence_palindrome(s):
    fst, lst = 0, len(s) - 1
    s = s.lower()
    # Compares character until they are equal
    while fst <= lst:
        # If there is another symbol in left of sentence
        if not (s[fst] >= 'a' and s[fst] <= 'z'):
            fst += 1
        # If there is another symbol in right of sentence
        elif not (s[lst] >= 'a' and s[lst] <= 'z'):
            lst -= 1
        # If characters are equal
        elif s[fst] == s[lst]:
            fst += 1
            lst -= 1
        # If characters are not equal then sentence is not palindrome
        else:
            return False
    return True


s = "Too hot to8908 hoot."
if sentence_palindrome(s):
    print("Sentence is palindrome.")
else:
    print("Sentence is not palindrome.")