# Function to find permutations of a given string
from itertools import permutations, groupby, combinations


def proper_str(data):
    if data.startswith('-'):
        data1 = data.replace('-', "")
        return data1
    elif '-' in data:
        return 0
    else:
        return data


sw = ''
# string_given = 'co?3d5er45,3'  # here can replace if you want any string
# string_given = 'g4e3e5k3s4'
# string_given = 'nu23m-2'
string_given = '-nknk4n4u23m-2'
req_data = proper_str(string_given)
if req_data:
    for num in list(req_data):
        w = ''
        if num.isdigit():
            w += num
        sw += w
    # print(type(sw))
    permList = permutations(sw)
    all_list = [''.join(perm) for perm in list(permList)]
    list_num = [int(x) for x in all_list if x == x[::-1]]
    print(max(list_num))
else:
    print(-1)

