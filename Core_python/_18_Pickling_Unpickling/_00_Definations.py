"""
PICKLE — Python object serialization
The pickle module is used for implementing binary protocols for serializing and de-serializing a Python object structure
Pickling:
========
It is a process where a Python object hierarchy is converted into a byte stream.
Unpickling:
==========
It is the inverse of Pickling process where a byte stream is converted into an object hierarchy.
Module Interface :
=================
dumps() – This function is called to serialize an object hierarchy.
loads() – This function is called to de-serialize a data stream.
For more control over serialization and de-serialization, Pickler or an Unpickler objects are created respectively.

Constants provided by the pickle module :
========================================
pickle.HIGHEST_PROTOCOL:
-----------------------
This is an integer value representing the highest protocol version available. This is considered as the
 protocol value which is passed to the functions dump(), dumps().
pickle.DEFAULT_PROTOCOL:
-----------------------
This is an integer value representing the default protocol used for pickling whose value may be less than
the value of highest protocol.
Functions provided by the pickle module :
========================================
pickle.dump(obj, file, protocol = None, *, fix_imports = True)
This function is equivalent to Pickler(file, protocol).dump(obj). This is used to write a pickled
representation of obj to the open file object file.
The optional protocol argument is an integer that tells the pickler to use the given protocol.
The supported protocols are 0 to HIGHEST_PROTOCOL. If not specified, the default is DEFAULT_PROTOCOL.
 If a negative number is specified, HIGHEST_PROTOCOL is selected.

If fix_imports is true and protocol is less than 3, pickle will try to map the new Python 3 names to the old
module names used in Python 2, so that the pickle data stream is readable with Python 2
"""
"""
Example :
--------
# Python program to illustrate 
# pickle.dump() 
import pickle
from StringIO import StringIO

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO 
out_s = StringIO()

# Write to the stream 
for o in data:
    print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()
Output :
=======
WRITING: pickle (elkcip)
WRITING: cPickle (elkciPc)
WRITING: last (tsal)
pickle.dumps(obj, protocol = None, *, fix_imports = True)
This function returns the pickled representation of the object as a bytes object.
Example :
========
# Python program to illustrate 
#Picle.dumps() 
import pickle

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
data_string = pickle.dumps(data)
print 'PICKLE:', data_string
Output :
========
PICKLE: (lp0
         (dp1
         S'a'
         p2
         S'A'
         p3
         sS'c'
         p4
         F3.0
         sS'b'
         p5
         I2
         sa.
3.pickle.load(file, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
This function is equivalent to Unpickler(file).load(). This function is used to read 
a pickled object representation from the open file object file and return the reconstituted object hierarchy specified.

Example :
========
# Python program to illustrate 
# pickle.load() 
import pickle
from StringIO import StringIO

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO 
out_s = StringIO()


# Write to the stream 
for o in data:
    print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()


# Set up a read-able stream 
in_s = StringIO(out_s.getvalue())

# Read the data 
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ: %s (%s)' % (o.name, o.name_backwards)
Output :
========
WRITING: pickle (elkcip)
WRITING: cPickle (elkciPc)
WRITING: last (tsal)
READ: pickle (elkcip)
READ: cPickle (elkciPc)
READ: last (tsal)

4.pickle.loads(bytes_object, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
This function is used to read a pickled object representation from a bytes object and return the reconstituted object hierarchy specified.
Example :
========
# Python program to illustrate 
# pickle.loads() 
import pickle
import pprint

data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'BEFORE:',
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print 'AFTER:',
pprint.pprint(data2)

print 'SAME?:', (data1 is data2)
print 'EQUAL?:', (data1 == data2)
Output :
========
BEFORE:[{'a': 'A', 'b': 2, 'c': 3.0}]
AFTER:[{'a': 'A', 'b': 2, 'c': 3.0}]
SAME?: False
EQUAL?: True

Exceptions provided by the pickle module :
=========================================
1.exception pickle.PickleError:
-------------------------------
This exception inherits Exception. It is the base class for all other exceptions raised in pickling.
2.exception pickle.PicklingError:
--------------------------------
This exception inherits PickleError. This exception is raised when an unpicklable object is encountered by Pickler.
3.exception pickle.UnpicklingError:
-----------------------------------
This exception inherits PickleError. This exception is raised when there is a problem like
 data corruption or a security violation while unpickling an object.
"""