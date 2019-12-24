class Car:
    company = 'Tesla'
    year = 2020
    car_count = 0

    def __init__(self, modle, bhp, fuel):
        self.modle = modle
        self.bhp = bhp
        self.fuel = fuel
        Car.car_count += 1

    def __str__(self):
        return f"Car Model:{self.modle}   BHP:{self.bhp}   Fuel:{self.fuel}"

    @classmethod
    def get_detail(cls):
        return f"Company:{Car.company}  Year:{Car.year}  Car count:{Car.car_count}"


c1 = Car('GTS', 2500, 'petrol')
c2 = Car('G9', 2000, 'diesel')
c3 = Car('GTS', 2100, 'petrol')
c4 = Car('S5', 2200, 'diesel')
c5 = Car('G3', 2700, 'petrol')
c6 = Car('T6', 2600, 'diesel')
# a.get_detail()
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(Car.get_detail(), '\n', type(Car.get_detail()))
