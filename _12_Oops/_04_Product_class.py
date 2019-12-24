class Product:
    company = 'Prestage'
    pcount = 0

    def __init__(self, barcode, name, quantity, price, discount=0):
        self.barcode = barcode
        self.name = name
        self.quantity = quantity
        self.price = price
        self.disc = discount
        Product.pcount += 1

    def __str__(self):
        return f"Barcode:{self.barcode} Name:{self.name} Quantity:{self.quantity} " \
               f"Price:{self.price} Discount:{self.disc}"

    def disc_price(self, disc_amt, quant):
        self.price = self.price * quant
        self.price -= ((disc_amt / 100) * self.price * quant)
        return self.price

    def net_amt(self, quant):
        self.price = self.price * quant
        return self.price

    @classmethod
    def get_prod(cls):
        return f"Company:{Product.company}  product Count:{Product.pcount}"


cooker = Product(10120, 'Cooker s9', 6, 1850, 15)
building = Product(10125, 'Building Apartment', 5, 185000, 10)
tv1 = Product(10121, 'Tv', 6, 18500, 12)
trimmer = Product(10100, 'Trimmer s8', 2, 2000, 15)
watch = Product(10102, 'Watch', 4, 1900, 10)
tv2 = Product(10123, 'Tv', 8, 26000, 20)
cooker.disc_price(15, 2)
print(cooker)
k = cooker.net_amt(5)
print('Net Amount:', cooker.net_amt(6))
print(Product.get_prod())
