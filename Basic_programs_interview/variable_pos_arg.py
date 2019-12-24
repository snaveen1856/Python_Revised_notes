# variable positional argument
def sum_l(* num):
    if num:
        total = 0
        for i in num:
            total += i
        return total


t = sum_l(3, 12, 18, 56, 14, 13, 48, 59, 46, 3)
print(t)
s = sum_l(56, 18)
print(s)
n = sum_l()
print(n)
