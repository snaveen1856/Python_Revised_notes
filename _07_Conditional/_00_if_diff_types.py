"""
if Condition will have three types. They are :
1. Simple if
2. if - else
3. Nested if
Here the examples of the three conditions
Examples:
=========
Simple-if
=========
a = 2
b = 330
print("A") if a > b else print("B")

if-else:
=======

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
===============================================
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
====================================================
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

Nested-if condition:
====================
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
  print("Below ten")
  if x < 5:
    print(" And also below 5!")
  else:
    print("But not below 5!")

"""