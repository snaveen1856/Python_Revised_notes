"""
1. palindrome swapper
ex:1
"""
import itertools


def palindrome_swapper(string):
    # p = list(''.join(string.lower().split()))
    p = ''.join(string.lower().split())
    print(p)
    s = False
    l1 = []
    for i in range(len(p) - 1):
        l2 = list()


palindrome_swapper('Ram')

"""
2. Run length of string
"""


def runlength(string):
    res = ''
    for k, g in itertools.groupby(string):
        # print(k, g)
        res = res + k + str(len(list(g)))
    return res


print(runlength('wwwdesw'))
