def add(num1, num2):
    return num1 + num2


def add_only_postive(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 + num2
    else:
        return None


if __name__ == "__main__":
    print(add(5, 3))
    print(add_only_postive(5, 6))
    print(add_only_postive(-3, 5))
