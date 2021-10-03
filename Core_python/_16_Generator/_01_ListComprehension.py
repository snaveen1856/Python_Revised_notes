#  https://www.programiz.com/python-programming/list-comprehension
"""
List Comprehension :
-------------------
 => List comprehensions provide a concise way to create lists

For loop vs List Comprehension :

REQ : Separate the letters of the word human and add the letters as items of a list.
"""
# Example 1: Iterating through a string Using for Loop

h_letters = []  # 1. CREATE A EMPTY LIST

for letter in 'human':  # 2. ITERATE THROUGH SEQUENCE
    h_letters.append(letter)  # 3. APPENDING EACH ELEMENT INTO LIST

print("--Using for loop--------------", h_letters)

# Example 2: Iterating through a string Using List Comprehension

h_letters = [letter for letter in 'human']

print("--Using list comprehension----", h_letters)

val = [x ** x for x in range(5)]

print("--Using list comprehension----", val)

'''
Syntax of List Comprehension : [<output expression> <for item in sequence> <Conditions>]
                             Ex: [ letter for letter in 'human' ]
                                                 
List comprehension  can identify when it receives a string or a tuple and work on it like a list.
'''

# Using if with List Comprehension :
print("=========IF with List Comprehension==============")
number_list = [x for x in range(20) if x % 2 == 0]  # x
# for x in range(20)
# if x % 2 == 0                                                                                                        
print("MAD=", number_list)
print("-------------OR--------------")
number_list = []
for x in range(20):
    if x % 2 == 0:
        number_list.append(x)
# Nested IF with List Comprehension
print("=========Nested IF with List Comprehension==============")
num_list = [y ** 2 for y in range(100) if y % 2 == 0 if y % 5 == 0]  # y
# for y in range(100)
#    if y % 2 == 0
#         if y % 5 == 0
print("Using comprehension : ", num_list)

print("-------------OR--------------")
number_list = []
for y in range(100):
    if y % 2 == 0:
        if y % 5 == 0:
            number_list.append(y ** 2)
print("Using for loop      : ", number_list)

# if...else With List Comprehension
print("========= if...else  with List Comprehension==============")

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

print("-------------OR--------------")
obj = []
for i in range(10):
    if i % 2 == 0:
        obj.append("Even")
    else:
        obj.append("Odd")
print(obj)

print("----List comprehension with expression------------")

list1 = [3, 4, 5]
multiplied = [item * 5 for item in list1]
print(multiplied)

square = [item * item for item in list1]
print(square)
'''
Key Points :
============
1.List comprehension is an elegant way to define and create lists based on existing lists.
2.List comprehension is generally more compact and faster than normal functions and 
   loops for creating list.
3.However, we should avoid writing very long list comprehensions in one line to ensure. 
   that code is user-friendly.
4.Every List comprehension can be rewritten in for loop but vice versa is not true.
 '''
