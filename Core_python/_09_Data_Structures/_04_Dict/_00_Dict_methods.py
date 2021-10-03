"""
Python has a set of built-in methods that you can use on dictionaries.

Method	              Description
=============================================================================================================
clear()=========> Removes all the elements from the dictionary
copy()==========> Returns a copy of the dictionary
items()=========> Returns a list containing a tuple for each key value pair
keys()==========> Returns a list containing the dictionary's keys
values()========> Returns a list of all the values in the dictionary
get()===========> Returns the value of the specified key
setdefault()====> Returns the value of the specified key.If the key does not exist insert the key with the specified value
fromkeys()======> Returns a dictionary with the specified keys and values
has_key()=======> Removed, use the in operation instead
pop()===========> Removes the element with the specified key
popitem()=======> Removes the last inserted key-value pair
update()========> Updates the dictionary with the specified key-value pairs
"""
d = {'name': 'Sindhu', 'empno': 7081, 'sal': 85000, 'comp': 'GSS'}
print(d)
s = d.copy()
# dict_from = d.fromkeys()
# k = d.setdefault('addr', default='cyber pearl')
print('S dict:', s)
s['PF'] = 12345678987654
print('S dict:', s)
s.pop('PF')
print('S dict:', s)
s.popitem()
print('S dict:', s)
# print(d)
# print(k)
