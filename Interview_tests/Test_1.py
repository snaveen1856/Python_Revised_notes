def xyz():
    print([lambda x: i * x for i in range(4)])
    return [lambda x: i * x for i in range(4)]


def Ram(i=[]):
    i.append(1)
    return i


print([m(2) for m in xyz()])
print(Ram())
print(Ram())
