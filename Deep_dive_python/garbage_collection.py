# Garbage Collection
""" - can be controlled programmatically using the 'gc' module by default it is turned ON.
    - you may turn it OFF if you are sure your code does not create circular references but Beware.
    - Run periodically on  its own (if turned ON)
    - you can call it manually and even do your own clean up 
    In general GC works just fine.
    for python 3.4 and above if even one of the objects in the circular reference has a destructure 
    eg. __del__()
    the destructure order of the objects may be important but the GC does not know what that order
    should be so the object is marked as UNCOLLECTABLE
    and the objects in the circular reference are not cleaned up  ---> Memory leak.
"""

# Circular References

import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not Found"


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: self: {hex(id(self))}, b: {hex(id(self.b))}')


class B:
    def __init__(self, a):
        self.a = a 
        print(f'B: self: {hex(id(self))}, a: {hex(id(self.a))}')


gc.disable()
my_var = A()
