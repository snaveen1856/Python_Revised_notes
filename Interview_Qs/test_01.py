
number_of_customers = int(input("Enter number of customers :"))
s_p = []
for i in range(1, number_of_customers + 1):
    size_price = input("Enter shoe size and price: ").split(" ")
    s_p.append(size_price)

print(s_p)  # [['6', '55'], ['6', '45'], ['6', '55'], ['4', '40'], ['18', '60'], ['10', '50']]

