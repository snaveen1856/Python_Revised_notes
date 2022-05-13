"""
d1 ={'ten':'a','two':'b','one':'a','three':'b'}
class with init and instance methods.create object get methods
lambda function to show even numbers using filter function
different models in django
django advantages disadvantages
flask vs django
sql injection attacks
how to resolve performance issues in django
django loosely coupled how
proxy model in django
python multi-threading disadvantages

REQ:
---------
python django robot modules belongs to storage
"""


def xyz():
    return [lambda x: i * x for i in range(4)]


def Ram(i=[]):
    i.append(1)
    return i


print(xyz())
print([m(2) for m in xyz()])
print(Ram())
print(Ram())


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
