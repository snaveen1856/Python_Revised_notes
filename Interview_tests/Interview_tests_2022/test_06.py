# '1000100110000100000101000000'
s = 0b1000100110000100000101000000
num = int(input('Enter a number: '))
if isinstance(num, int):
    string = str(bin(num))
    req_lst = string[2:]
    st = [len(i) for i in req_lst.split('1')]
    if req_lst.startswith('1') and req_lst.endswith('1'):
        print('Binary code of given number:', string)
        print('Maximum no. of zeros are:', max(st))
    elif not req_lst.endswith('1'):
        st.pop()
        print('Binary code of given number:', string)
        print('Maximum no. of zeros are:', max(st))
else:
    print('Enter number only: ')

print('==================================================================')


def route_fun(arr, key):
    if isinstance(key, int):
        if key == 0:
            print('Given string:', arr)
            return arr
        else:
            print('Given string:', arr)
            result_01 = arr[:key - 1]
            result_02 = arr[key - 1:]
            result_02.extend(result_01)
        return result_02
    else:
        return f'Please enter array and number as key'


array_ = [1, 8, 5, 9, 10, 4, 2, 6]
key = 3
ans = [9, 10, 4, 2, 6, 1, 8, 5]
print(route_fun(array_, key))
