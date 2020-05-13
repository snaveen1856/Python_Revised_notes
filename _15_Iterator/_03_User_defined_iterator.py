class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# case 1
# c = Counter(1, 5)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# # print(next(c))

# case 2
c = Counter(1, 8)
iterator = iter(c)
while True:
    try:
        x = iterator.__next__()
        print(x, end='')
    except StopIteration as err:
        break
