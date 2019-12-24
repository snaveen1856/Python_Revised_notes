# 2. NESTED FUNCTIONS :
# =====================
print("---------------2. NESTED FUNCTIONS------------------")


def parent1():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(second_child())
    print(first_child())


parent1()  # Here there is no reference add.. so, the return value will collected by grabage
# parent1.first_child()
try:
    parent1.first_child()
except AttributeError as err:
    print("------You cannot call nested function directly------------")

print("---------------------------------------------------")
