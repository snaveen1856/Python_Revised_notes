#  https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/
"""
python 2.7
-----------
range Iterator  - Iterator
xrange generator - Generator

range - Generator
"""
"""
Different b/w Python 2.x to python 3.x:

Python 2.7                                      Python 3.7
==============================================================================
1. print "something"                        1. print("something")
2. raw_input() default string               2. input() string only
3. implicit string is ASCII                 3. implicit string is UNICODE
4. Xrange() function like iterator          4. range() function returns list
like java.
5. syntax for Division 5/2 = 2 only int     5. Here only int division value 5//2 = 2 and true division 5/2 = 2.5 
"""