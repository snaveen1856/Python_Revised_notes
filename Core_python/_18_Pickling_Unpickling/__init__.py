"""
import pickle
d={'Name':'Naveen','Course':'Python','fee':25000}
"""


def is_palindrome(word, in_pos):
    try:
        if len(word) >= in_pos:
            print("Position with", in_pos, " value is :", word[in_pos - 1])
        else:
            raise ValueError("Value does not exist")
        for each in range(0, len(word)):
            if word[each] != word[len(word) - each - 1]:
                return False
            return True
    except Exception as e:
        print("Value does not exist with give index.", e)


in_str = input("Enter any string :")
pos = int(input("Enter position of required val :"))
print("Given word Palindrome : ", is_palindrome(in_str, pos))
