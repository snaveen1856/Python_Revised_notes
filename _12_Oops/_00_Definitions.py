"""

Class             : A user-defined prototype for an object that defines
-----               a set of attributes that characterize any object of the class.
                  : A user defined data type and it is a blueprint of object.
                    The attributes are:
                    1.data members/FIELDS(class variables and instance variables)  {STATES}
                    2.method( accessed via dot notation)                           {BEHAVIORS}

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
Hiding the implementation details in the methods of  a class

In a "Normal class" Abstraction is 0%
In "Abstract Class" Abstraction is 0-100 %
In an "Interface"   Abstraction is 100%

Inheritance :
------------
The transfer of the characteristics of a class to other classes that are derived from it.(super class ,sub class)
        *If the two objects have "is a" relationship then use inheritance.
        *If the two objects have "has a" relationship then use inheritance.
            Types of inheritance
            1.single level  2.multi-level  3.Hirareical  4.Multiple

Polymorphism :
---------------
    - Static Polymorphism -- Method overloading
    - Dynamic Polymorphism -- Method overriding
    
"""