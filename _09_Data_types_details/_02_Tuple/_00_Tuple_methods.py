"""
Tuples:
=======
A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to
a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.

# An empty tuple
empty_tuple = ()
print (empty_tuple)
Output:
------
# Creating non-empty tuples
# One way of creation
tup = 'python', 'geeks'
print(tup)

# Another for doing the same
tup = ('python', 'geeks')
print(tup)
Output:
------
('python', 'geeks')
('python', 'geeks')
Note: In case your generating a tuple with a single element, make sure to add a comma after the element.
concatenation of Tuples

# Code for concatenating 2 tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

# Concatenating above two
print(tuple1 + tuple2)
Output:
------
(0, 1, 2, 3, 'python', 'geek')

Nesting of Tuples:
------------------
# Code for creating nested tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)
Output :
--------
((0, 1, 2, 3), ('python', 'geek'))


Repetition in Tuples:
---------------------
# Code to create a tuple with repetition

tuple3 = ('python',)*3
print(tuple3)
Output:
------
 ('python', 'python', 'python')
Try the above without a comma and check. You will get tuple3 as a string ‘pythonpythonpython’.

Immutable Tuples:
================
#code to test that tuples are immutable

tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)
Output:
------
Traceback (most recent call last):
  File "e0eaddff843a8695575daec34506f126.py", line 3, in
    tuple1[0]=4
TypeError: 'tuple' object does not support item assignment


Slicing in Tuples:
=================
# code to test slicing

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
Output

(1, 2, 3)
(3, 2, 1, 0)
(2, 3)


Deleting a Tuple:
=================
# Code for deleting a tuple

tuple3 = ( 0, 1)
del tuple3
print(tuple3)
Error:
-----
Traceback (most recent call last):
  File "d92694727db1dc9118a5250bf04dafbd.py", line 6, in <module>
    print(tuple3)
NameError: name 'tuple3' is not defined
Output:
------
(0, 1)


Finding Length of a Tuple:
=========================
# Code for printing the length of a tuple

tuple2 = ('python', 'geek')
print(len(tuple2))
Output:
------
 2


Converting list to a Tuple:
===========================

# Code for converting a list and a string into a tuple

list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python')) # string 'python'
Output:
------
(0, 1, 2)
('p', 'y', 't', 'h', 'o', 'n')
Takes a single parameter which may be a list,string,set or even a dictionary( only keys are taken as elements)
 and converts them to a tuple.
Tuples in a loop:
================
#python code for creating tuples in a loop

tup = ('geek',)
n = 5  #Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup)
Output :
--------
(('geek',),)
((('geek',),),)
(((('geek',),),),)
((((('geek',),),),),)
(((((('geek',),),),),),)


Using cmp(), max() , min():
==========================
# A python program to demonstrate the use of
# cmp(), max(), min()

tuple1 = ('python', 'geek')
tuple2 = ('coder', 1)

if (cmp(tuple1, tuple2) != 0):

    # cmp() returns 0 if matched, 1 when not tuple1
    # is longer and -1 when tuple1 is shoter
    print('Not the same')
else:
    print('Same')
print ('Maximum element in tuples 1,2: ' +
        str(max(tuple1)) +  ',' +
        str(max(tuple2)))
print ('Minimum element in tuples 1,2: ' +
     str(min(tuple1)) + ','  + str(min(tuple2)))
Output:
------
Not the same
Maximum element in tuples 1,2: python,coder
Minimum element in tuples 1,2: geek,1
Note: max() and min() checks the based on ASCII values. If there are two strings in a tuple,
 then the first different character in the strings are checked.

Python has two built-in methods that you can use on tuples.

Method	               Description
--------------------------------------------------------------------------------------
1.count() ======> Returns the number of times a specified value occurs in a tuple
2.index() ======> Searches the tuple for a specified value and returns the position of where it was found
3. len() =======> returns the length of tuple
"""
t = (1, 2, 3, 4, 5)
t1 = (1,)
print(t, '\n ', t1)