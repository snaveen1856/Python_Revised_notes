# user defined function and different type calling a function #######=====> this is also method overloading
def print_num(start=1, end=10, step=1):
    for i in range(start, end, step):
        print(i, end=' ')
    print()


print_num()
print_num(5)
print_num(10, 21)
print_num(10, 100, 10)
print_num(end=21)
print_num(step=2)
print_num(2, step=3)
