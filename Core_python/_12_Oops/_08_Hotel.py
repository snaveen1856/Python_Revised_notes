class Hotel:
    """ This is hotel billing code
    """
    hotel_name = 'Surya-Ganga'
    customer_count = 0
    net_pay = 0

    def __init__(self, bill_no, name, bill_amt, discount=0):
        self.bill_no = bill_no
        self.name = name
        self.bill_amt = bill_amt
        self.discount = discount
        Hotel.customer_count += 1

    def __str__(self):
        return f"Billno={self.bill_no} Name={self.name} Bill-Amt={self.bill_amt} Discount={self.discount}"

    def set_discount(self):
        if self.bill_amt >= 1500:
            self.discount = 0.1
        elif self.bill_amt >= 2000:
            self.discount = 0.15
        elif self.bill_amt >= 2500:
            self.discount = 0.2
        elif self.bill_amt >= 3500:
            self.discount = 0.25
        else:
            self.discount = 0.05
        return self.discount

    def amt_pay(self):
        Hotel.net_pay = self.bill_amt - (self.discount * self.bill_amt)
        return Hotel.net_pay

    @classmethod
    def net_paid(cls):
        print(f"Hotel name:{Hotel.hotel_name}  Net pay:{Hotel.net_pay}")


s1 = Hotel(120, 'Sindhu B', 1500)
s1.set_discount()
print(s1)
# print(sindu.set_discount())
s1.amt_pay
# print(sindu.amt_pay)
print(id(s1))
print(Hotel.net_pay)
print('-' * 40)
print(Hotel.customer_count, Hotel.hotel_name)
Hotel.net_paid()
print(s1.amt_pay())
