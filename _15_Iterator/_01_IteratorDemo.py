list1 = ['a', 'b', 'c', 'd']

del (list1[0])
del (list1[-2:])
print(list1)
print(dir(list1))
print(dir(3))
'''
['__add__'   +
'__class__'
'__contains__'
'__delattr__'
'__delitem__'
'__dir__'
'__doc__'
'__eq__'   ==
'__format__'
'__ge__'   >=
'__getattribute__'
'__getitem__'
'__gt__'    >
'__hash__'  
'__iadd__'
'__imul__'
'__init__'  
'__init_subclass__'
'__iter__' 
'__le__'    <=
'__len__'   
'__lt__'    <
'__mul__'    *
'__ne__'     !=
'__new__'     
'__reduce__'
'__reduce_ex__'
'__repr__'    
'__reversed__'  
'__rmul__'
'__setattr__'
'__setitem__'
'__sizeof__'
'__str__'      
'__subclasshook__'
'append'
'clear'
'copy'
'count'
'extend'
'index'
'insert'
'pop'
'remove'
'reverse'
'sort'
]
'''

# https://www.codementor.io/sheena/python-generators-and-iterators-du1082iua


print('__iter__' in dir([1, 2, 3]))  # returns True
print('__iter__' in dir((1, 2, 3)))  # returns True
print('__iter__' in dir(range(3)))  # returns True
print('__iter__' in dir(3))  # returns False
'''
for i in 3:
    print(i)
'''
# 1. For Loops Behind the Scenes

print("------------")
mylist = [1, 2, 3]
for i in mylist:
    # print(i)
    pass
print("------------")

myIterator = mylist.__iter__()  # myIterator is a listiterator object.

# while True:
#    print(myIterator.__next__())
'''
For loops loop over iterables.
iterables have __iter__ functions
__iter__ functions return Iterators
Iterators make use of the next method to move from element to element within their associated iterable
once an iterator runs out of things to return from the next function it raises the StopIteration exception
 whenever next is called
'''

print("------------")


def my_for_loop(some_iterable):
    oIter = some_iterable.__iter__()
    while True:
        try:
            print(oIter.__next__())
        except StopIteration:
            break


my_for_loop([1, 2, 3])


# 2. Using __iter__ to Make Iterators from Your Objects
class FibIterable:
    """
    this class is a generates a well known sequence of numbers 
    """

    def __init__(self, iLast=1, iSecondLast=0, iMax=500):
        self.iLast = iLast
        self.iSecondLast = iSecondLast
        self.iMax = iMax  # cutoff

    def __iter__(self):
        return self  # because the object is both the iterable and the iterator

    def __next__(self):
        iNext = self.iLast + self.iSecondLast
        if iNext > self.iMax:
            raise StopIteration()
        self.iSecondLast = self.iLast
        self.iLast = iNext
        return iNext


print("----------My own customized Iterator through AUTO------------")
myObj = FibIterable()  # list1 = [1,2,3]

for value in myObj:
    print(value)

print("----------My own customized Iterator through MANUAL------------")
myObj1 = FibIterable()
myObjItearartor = myObj1.__iter__()
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
print(myObjItearartor.__next__())
# print(myObjItearartor.__next__())
'''Steps implemented above
1. we initialised an object , myObj of class FibIterable.
2. The for loop called myObj.__iter__ which just returned myObj
3. For each iteration of the for loop, the loop called myObj.next() which calculated the next value in the sequence
4. if the next value was too high then the next raised a StopIteration in order to break out of the loop
   otherwise the changed state of myObj was stored and the correct next value was returned.
   
Finally,
You can write for loops for iterating over many kinds of Python's build in iterables and, if that's not enough,
 you can even make your own iterables.
'''
