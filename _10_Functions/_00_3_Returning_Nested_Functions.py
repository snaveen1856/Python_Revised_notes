# 3. RETURNING FUNCTIONS:
# ======================
print("---------------3. RETURNING NESTED FUNCTION NAME------------------")


def parent(num):
    def first_child(message):
        return "Printing from the first_child() function.", message

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        print("Assertion is True.Continue to execute the remaining code")
        return first_child  # returning function name
    except AssertionError:
        return second_child  # returning function name
    finally:
        print("Finally executed")


xyz = parent(10)

print("******************************************")
print("Returning function name fc", xyz)
print("Executing function foo  ", xyz("HELLO WORLD"))
print("*************")

abc = parent(11)
print("Returning function name bar ", abc)
print("Executing function bar     ", abc())
