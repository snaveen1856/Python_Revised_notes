def conv_list_tuple(l):
    if not l:
        print('Given argument is Not a List!')
    t = tuple()
    t = tuple(l)
    return t


def conv_tuple_list(t):
    if not t:
        print('Given argument is Not a Tuple!')
    l = []
    for i in t:
        l.append(i)
    return l


def conv_list_set(l):
    if not l:
        print('Given argument is not list!')
    s = set()
    for i in l:
        s.add(i)
    return s


def conv_set_list(s):
    if not s:
        print('Given argument is not set!')
    l = []
    for i in s:
        l.append(i)
    return l


# s=(1,2,3,5)
# print(s)
# n=conv_tuple_list(s)
# print(n)

l = [7, 8, 9, 4, 4]
c = conv_list_tuple(l)
print(c)
m = conv_list_set(l)
print(m)
g = conv_set_list(m)
print(g)
