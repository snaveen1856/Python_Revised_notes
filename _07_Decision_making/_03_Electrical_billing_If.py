# Electric Billing

units = int(input('Enter number of units:'))
if units <= 100:
    amount = units * 2.50
elif units <= 300:
    amount = 100 * 2.50 + (units - 100) * 3.50
elif units <= 500:
    amount = 100 * 2.50 + 200 * 3.50 + (units - 300) * 5
else:
    amount = 100 * 2.50 + 200 * 3.50 + 200 * 5.0 + (units - 500) * 6.50
print(f"Electric units:{units} \nBill Amount:{amount}")
