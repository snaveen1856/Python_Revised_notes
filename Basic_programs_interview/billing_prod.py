# Billing of product

Amount = float(input("Enter amount:"))
Discount = 0.0
if 4000 < Amount < 4999:
    Discount = 0.1
elif 5000 < Amount < 5999:
    Discount = 0.15
elif Amount > 6000:
    Discount = 0.2
else:
    Discount = 0.05

Discount_Amount = Amount * Discount
Net_Amount = Amount - Discount_Amount
print('{:20s}:{:10.2f}'.format('Amount', Amount))
print('{:20s}:{:10.2f}'.format('Discount_Amount', Discount_Amount))
print('_' * 40)
print('{:20s}:{:10.2f}'.format('Net_Amount', Net_Amount))
print('_' * 40)
