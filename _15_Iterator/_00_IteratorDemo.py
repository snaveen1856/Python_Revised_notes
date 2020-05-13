from email import iterators

# https://www.programiz.com/python-programming/iterator
list1 = [1, 2, 3, 4]
print(list1[2])

for i in [1, 2, 3, 4]:
    print(i)

'''
1. List object will be created.
2. On same object __iter__() or iter() method will be called
   We will get iterator object.
3. On iterator object __next__ or next()  method will be called 
    so that we will get elements one by one in sequence.
'''
'''
__iter__() // - iter()   Method calling both ways
__next__() // - next()   Method calling both ways

String,list,tuple, set, Zip, map, filter, range, bytes, byte array and yield  are Sequence type.
int,float,complex are Number type.
String, tuple, dict.keys(), float and int are Immutable data types 
List, set, dict.values()  are Mutable data types.
list1 - iterable object
list1.__iter__() ==> iterator   .__next__()
'''
'''
Python Iterators :
-----------------
Iterators are the objects that can be iterated upon. 
Let us see how iterator works and how you can build your own iterator
 using __iter__ and __next__ methods.

1.What are iterators in Python?
===============================
  => Iterator in Python is simply an object that can be iterated upon. 
     An object which will return data, one element at a time.
  => Iterators are everywhere in Python. They are elegantly implemented within for loops,
     comprehensions, generators etc. but hidden in plain sight.
  => Technically speaking, Python iterator object must implement two special methods, 
                  __iter__() and 
                  __next__(), 
                  collectively called the iterator protocol.
  => An object is called iterable if we can get an iterator from it. 
     Most of built-in containers in Python like: list, tuple, string etc. are iterables.
  => iter() function (which in turn calls the __iter__() method) returns an iterator from them.

2. Iterating Through an Iterator in Python:
===========================================
  => We use the next() function to manually iterate through all the items of an iterator. 
     When we reach the end and there is no more data to be returned, it will raise StopIteration
'''

my_list = [4, 7, 0, 3]  # 1. Define a list
my_iter = my_list.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("---------Iterator Internal Mechanism-----------")
print(my_iter.__next__())  # 3. Iterate through it using __next()__
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())  # This will raise error, as no items left in my_list
# print(my_iter.__next__())  
# print(next(my_iter))                ### next(obj) is same as obj.__next__()

print("---------Iterator For loop Mechanism-----------")
for val in my_list:
    print(val)

'''
3. How for loop actually works?
  => As we see in the above example, the for loop was able to iterate automatically through the list.
  => In fact the for loop can iterate over any iterable. 
     Let's take a closer look at how the for loop is actually implemented in Python.
     
  for element in iterable:
    # do something with element
                                       Is actually implemented as.


iter_obj = iter(iterable)            # create an iterator object from that iterable

while True:                          # infinite loop
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
        
    So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

Ironically, this for loop is actually an infinite while loop.

Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. 
After all the items exhaust, StopIteration is raised which is internally caught and the loop ends. 
Note that any other kind of exception will pass through.
'''

'''
4. Building Your Own Iterator in Python
    => Building an iterator from scratch is easy in Python. 
       We just have to implement the methods __iter__() and __next__().
    => The __iter__() method returns the iterator object itself. 
       If required, some initialization can be performed.
    => The __next__() method must return the next item in the sequence. 
       On reaching the end, and in subsequent calls, it must raise StopIteration.
'''


# Here, we show an example that will give us next power of 2 in each iteration.
# Power exponent starts from zero up to a user set number.

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


print("-----PowTwo--------------")
# Now we can create an iterator and iterate through it as follows.
myObj = PowTwo(4)
myIter = iter(myObj)
print(next(myIter))  # or myIter.__next()__
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

print("--------OR----------")
for i in PowTwo(4):
    print(i)
print(type(range))