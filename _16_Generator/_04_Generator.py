a = [1, 2, 3, 4]
print('list a:', a)
print('Reverse of list:', a[::-1])
result = [x * 2 for x in range(10)]
print('Result list', result, 'Type of result:', type(result))

# Iterator vs Generator
# http://nvie.com/posts/iterators-vs-generators/

from itertools import islice

# ITERATOR
for i in [1, 2, 3, 4]:
    print(i)
    print('------------')
for c in "python":
    print(c)
    print('------------')
for k in {'x': 1, 'y': 2}:
    print(k)
    print('------------')

'''ITERATION PROTOCOL :: 
======================
The built-in function iter takes an iterable object and returns an iterator.
    x=iter([1,2,3])
    x.next() -- 1
    x.next() -- 2  IF no more elements :: StopIteration
   '''


class yrange:
    def __init__(self, n):
        print("in init() method")
        self.i = 0
        self.n = n

    def __iter__(self):
        print("in iter() method")
        return self

    def next(self):
        print("in next() method")
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


y = yrange(3)
print(y.next())
print(y.next())
print(y.next())
# print(y.next())
# l=list(yrange(5))

result = (x for x in range(10))
print("M", type(result))
val = sum(x * x for x in range(1, 3))
print(val)

'''GENERATOR  : Any generator also is an iterator (not vice versa!);
                Any generator, therefore, is a factory that lazily produces values.
'''
print("---------------------Fibonacci Series---------------------")


def fib():
    prev, current = 0, 1
    while True:
        yield current  # The return value of the function will be a generator
        prev, current = current, prev + current


f = fib()  # the generator (the factory) is instantiated and returned.
# No code will be executed at this point:
# the generator starts in an idle state initially
print("Naveen")
# print(f())

print("Naveen", list(islice(f, 0, 10)))
print("---------------------Fibonacci Series---------------------")

'''
islice is an iterator,wrapped inside list.
List wil consume all of its elements and builds list by calling next()
on islice instance,which in turn.
will start calling next() on our f instance            
'''
'''
TWO TYPES OF GENERATORS 
1.GENERATOR FUNCTIONS   : Generator function is any function in which the 
                           keyword yield appears in its body.
2.GENERATOR EXPRESSIONS : Generator equivalent of a list comprehension
'''
numbers = [1, 2, 3, 4, 5]
list1 = []
for x in numbers:
    list1.append(x * x)
print("Iterator : ", list1)

# GENERATOR Expression
numbers = [1, 2, 3, 4, 5]

# LIST Comprehension :
print([x * x for x in numbers])

# SET Comprehension :
print({x * x for x in numbers})

# DICTIONARY Comprehension:
print({x: x * x for x in numbers})

# Generator Expr:
lazy_square = (x * x for x in numbers)
print(lazy_square)
print(next(lazy_square))
print(list(lazy_square))