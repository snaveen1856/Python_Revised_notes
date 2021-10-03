def get_price():
    while True:
        try:
            price = float(input('Enter price: '))
            return price
        except ValueError:
            print('Enter valid numbers only:')


def get_qty():
    while True:
        try:
            qty = int(input('Enter quantity: '))
            return qty
        except ValueError:
            print('Enter valid numbers only: ')


price = get_price()
quantity = get_qty()
total = price * quantity
print('Total amount: ', total)
