# Python3 code to demonstrate working of
# Unique dictionary filter in list 
# Using map() + set() + items() + sorted() + tuple() 

# Initialize list 
test_list = [
             {'gfg': 1, 'is': 2, 'best': 3},
             {'gfg': 1, 'is': 2, 'best': 3},
             {'gfg': 9, 'is': 8, 'best': 6}
            ]

# printing original list 
print("The original list is : " + str(test_list))

# Unique dictionary filter in list 
# Using map() + set() + items() + sorted() + tuple() 
res = list(map(dict, set(tuple(sorted(sub.items())) for sub in test_list)))

# printing result 
print("The list after removing duplicates : " + str(res))
