"""
list def:
--------
The list is mutable data-type and most versatile data-type available in Python which can be written as a list of
comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be
of the same Data-type.
ex:
l = [10,18.56,'Ram','s',18+56j]

Python has a set of built-in methods that you can use on lists/arrays.

Method	              Description
==========================================================
1.append()=======> Adds an element at the end of the list
2.extend()=======> Add the elements of a list (or any iterable), to the end of the current list
3.index() =======> Returns the index of the first, element with the specified value
4.insert()=======> Adds an element at the specified position # l1.insert(2,'Ram')
5.count()========> Returns the number of elements with the specified value
6.pop()==========> Removes the element at the specified position and it display the element
7.clear()========> Removes all the elements from the list
8.remove()=======> Removes the first, item with the specified value
9.copy()=========> Returns a copy of the list
10.reverse()======> Reverses the order of the list
11.sort()=========> Sorts the list i.e., arrange in ascending order

Maths functions like:
--------------------
Sum() ========> Sum of all number in the list
Max() ========> Max of number in list
min() ========> min of number in list
len() ========> return length of list

"""
l = [1, 2, 3, 4]
s = l.copy()
print(s)
print(l.index(3))