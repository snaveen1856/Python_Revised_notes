li_eq = [x ** x for x in range(10)]
print(li_eq)

'''
 http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

List comprehensions are a tool for transforming one list (any iterable actually) into another list.
 During this transformation, elements can be conditionally included in the new list and each element
  can be transformed as needed.
'''
# FOR LOOP
old_things = [1, 2, 3, 4, 5, 10, 11, 16, 20]
print('old list:', old_things)
new_things = []
for ITEM in old_things:
    if ITEM in range(1, 10):
        new_things.append(ITEM)
print(new_things)
# LIST COMPREHENSION
new_things = [ITEM for ITEM in old_things if ITEM in range(1, 10)]
print(new_things)

# SAME APPLIES TO SET AND DICT
