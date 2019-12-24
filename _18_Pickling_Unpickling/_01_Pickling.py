import pickle

my_list = ['a', 'b', 'c', 'd']
data = [[120, 'Naveen', 'Developer', 45000],
        [120, 'Kumar', 'Manager', 50000],
        [120, 'Sam', 'Designer', 48000],
        [120, 'John', 'Test', 46000]
        ]

dict1 = {'Id': 250, 'name': 'Naveen', 'Course': 'Python', 'fee': 25000}

a = dict(Id=125, name='Sindhu', Course='Python', fee=20000)

b = {12, 13, 18, 56, 18, 12, 13, 94, 45}

with open('datafile1.txt', 'wb') as fh:
    pickle.dump(data, fh)
