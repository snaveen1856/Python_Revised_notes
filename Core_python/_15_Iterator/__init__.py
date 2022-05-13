'''
Created on 19-Sep-2019

@author: Ram Kumar
'''

'''
EVERYTHING IS AN OBJECT IN PYTHON
'''
'''
Iterator : Speed consideration.

Generator : Memory Management 


2.X :   range()   : Iterator 
        xrange()  : Generator
 
3.X :   range()   : Generator

'''

for i in range(1000):
    print(i)

var = print("--------ITERATOR-----------")

for each in [1,2,3,4,5,6]:
    print("Element in list :",each)
    
l = [1,2,3,4,5,6]
for each in l:
    print("Element in list :",each)

'''
Iterator  --  When we require fater iteration. irrespective of memory contraints.
Generator --  When memory contraints exists.

Python 2.x
------------
range  - Iterator   -- Memory will be allocated for all 1L values
xrange - Generator  -- Memory will be created for one value at a time
                       0 - Memory X
                       1 - Memory X
                       2 - Momery
    
Python 3.x
------------
range - Generator

'''