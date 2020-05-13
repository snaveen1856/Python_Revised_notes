"""

Class             : A user-defined prototype for an object that defines
-----               a set of attributes which will characterize any object of the class.
                  : A user defined data type and it is a blueprint of object.
                    The attributes are:
                    1.data members/FIELDS(class variables and instance variables)         {STATES}
                    2.method( accessed via dot notation)(actions)                         {BEHAVIORS}

Encapsulation :
-----------------
Binding the data members(Fields,Variables,Attributes) & member methods(Methods(IM,CM,SM))
into single entity.
Example:
----------       
Class  ===> Logical  -- DATA(FIELDS)    
            Physical -- METHODS
Object ===> Physical -- DATA(FIELDS)    
            Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example

Abstraction :
--------------
Hiding the implementation details of the methods and data members of  a class

In a "Normal class" Abstraction is 0%
In "Abstract Class" Abstraction is 0-100 %
In an "Interface"   Abstraction is 100%

Inheritance :
------------
The transfer of the characteristics of a class to other classes that are derived from it.(super class ,sub class)
        *If the two objects have "is a" relationship then use inheritance.
        *If the two objects have "has a" relationship then use inheritance.
            Types of inheritance
            1.single level  2.multi-level  3.Hybrid   4.Multiple 5.Hierarchical

Polymorphism :
---------------
    - Static Polymorphism -- Method overloading
    - Dynamic Polymorphism -- Method overriding
    
"""

"""
Abstraction:
===========
Abstraction means hiding the complexity and only showing the essential features of the object. So in a way, Abstraction 
means hiding the real implementation and we, as a user, knowing only how to use it.

Real world example would be a vehicle which we drive with out caring or knowing what all is going underneath.

Ex: A TV set where we enjoy programs with out knowing the inner details of how TV works.

Abstraction in Python:
======================
Abstraction in Python is achieved by using abstract classes and interfaces.

An abstract class is a class that generally provides incomplete functionality and contains one or more abstract methods.
Abstract methods are the methods that generally don’t have any implementation, it is left to the sub classes to provide
implementation for the abstract methods.

Refer this post Abstract Class in Python to know more about abstract class in Python.
An interface should just provide the method names without method bodies. Subclasses should provide implementation for 
all the methods defined in an interface. 
==> Note that in Python there is no support for creating interfaces explicitly, 
you will have to use abstract class. In Python you can create an interface using abstract class. If you create an 
abstract class which contains only abstract methods that acts as an interface in Python.

Python abstraction example using abstract class
In the example there is an abstract class Payment that has an abstract method payment(). There are two child classes 
CreditCardPayment and MobileWalletPayment derived from Payment that implement the abstract method payment() as per their
 functionality.

As a user we are abstracted from that implementation when an object of CreditCardPayment is created and payment() 
method is invoked using that object, payment method of CreditCardPayment class is invoked. When an object of 
MobileWalletPayment is created and payment() method is invoked using that object, payment method of MobileWalletPayment 
class is invoked.

from abc import ABC, abstractmethod
class Payment(ABC):
    def print_slip(self, amount):
        print('Purchase of amount- ', amount)
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def payment(self, amount):
        print('Credit card payment of- ', amount)

class MobileWalletPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of- ', amount)

obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment))
obj = MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)
print(isinstance(obj, Payment))

Output:
======
Credit card payment of-  100
Purchase of amount-  100
True
Mobile wallet payment of-  200
Purchase of amount-  200
True
"""