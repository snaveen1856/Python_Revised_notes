list1 = [1, 2, 3, 4]
for list1[-1] in list1:
    print(list1)


def multiplexers():
    return [lambda n: index * n for index in range(4)]


print(len(multiplexers()))
print([m(2) for m in multiplexers()])

"""
Write a function `merge_dicts` that takes two dictionaries
as inputs and merges them into a single dictionary.
If there are duplicate keys between the two dictionaries, the
resultant dictionary's key should map to a list of the two
values obtained from each dictionary.

NOTE: Please do not use default dict. Your function should handle this.

e.g. 1 & TC 1:
_d1 = {1:2, 3:4, 'a':'b'}
_d2 = {0:1, 4:4, 10:'a'}
result = {1: 2, 3: 4, 'a': 'b', 0: 1, 4: 4, 10: 'a'}

e.g. 2 & TC 2:
_d1 = {1:2, 3:4, 10:5}
_d2 = {3:1, 4:4, 10:'a'}
result = {1: 2, 4: 4, 10: [5, 'a'], 3: [4, 1]}

e.g. 3 & TC 3:
_d1 = {1:2, 3:4, 'a':'b'}
_d2 = {3:1, 4:4, 10:'a', 'a':[1,2,3]}
result = {1: 2, 4: 4, 10: 'a', 'a': ['b', [1, 2, 3]], 3: [4, 1]}
"""


def merge_dict(dict1, dict2):
    req_result = dict1
    for key in dict2.keys():
        if key not in req_result:
            req_result[key] = dict2.get(key)
        else:
            if isinstance(req_result.get(key), list):
                req_result[key] = req_result.get(key).extends(dict2.get(key))
            else:
                req_result[key] = [req_result.get(key), dict2.get(key)]

    return req_result


# _d1 = {1:2, 3:4, 'a':'b'}
# _d2 = {0:1, 4:4, 10:'a'}
# _d1 = {1:2, 3:4, 10:5}
# _d2 = {3:1, 4:4, 10:'a'}
_d1 = {1: 2, 3: 4, 'a': 'b'}
_d2 = {3: 1, 4: 4, 10: 'a', 'a': [1, 2, 3]}
print(merge_dict(_d1, _d2))
