#  https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/
"""
Python 2.7
-----------
range Iterator  - Iterator
xrange generator - Generator

Python 3.7
----------
range - Generator
"""
"""
Different b/w Python 2.x to python 3.x:

Python 2.7                                      Python 3.7
==============================================================================
1. print "something"                        1. print("something")
2. raw_input() default byte string          2. input() default string 
3. implicit string is ASCII                 3. implicit string is UNICODE
    here all " " code strings.                  here byte string, string.
4. Xrange() function like iterator          4. range() function is generator
   like java.
5. syntax for Division 5/2 = 2 only int     5. Here only floor division value 5//2 = 2 and true division 5/2 = 2.5 
6. In exception, we use like                6. Here we use like as create an object for the exception
   try:                                           try:
      statements                                     statements
   except (Exception), e:                         except Exception as e:   
      print(e)                                          print(e)
"""