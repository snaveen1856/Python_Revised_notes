# infinite loop while (Factorial)

while True:
    n = int(input('Enter a number:'))
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"'{n}' factorial is {fact}")
    opt = input('compute to another number [y/n]:')
    if opt == 'n':
        break
