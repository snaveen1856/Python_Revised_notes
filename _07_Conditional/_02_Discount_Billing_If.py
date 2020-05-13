# Billing of product

Amount = float(input("Enter amount:"))
Discount = 0.0
if Amount > 4000:
    Discount = 0.1
elif Amount > 5000:
    Discount = 0.2
elif Amount > 8000:
    Discount = 0.3
else:
    Discount = 0.05
Discount_Amount = Amount * Discount
Net_Amount = Amount - Discount_Amount
print('{:20s}:{:10.2f}'.format('Amount', Amount))
print('{:20s}:{:10.2f}'.format('Discount_Amount', Discount_Amount))
print('_' * 40)
print('{:20s}:{:10.2f}'.format('Net_Amount', Net_Amount))
print('_' * 40)
