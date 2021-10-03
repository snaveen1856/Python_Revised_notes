class Engine:
    def __init__(self, Type, bhp):
        self.Type = Type
        self.bhp = bhp

    def show(self):
        print('Type: ', self.Type)
        print('BHP: ', self.bhp)


class Vehicle:
    def __init__(self, **kwargs):
        self.info = kwargs

    def show(self):
        for k, v in self.info.items():
            print(k, ':', v)


class Car(Vehicle):
    def __init__(self, **kwargs):
        self.fuel = kwargs.pop('fuel', 'Petrol')
        self.trans = kwargs.pop('trans', 'Manual')
        Type = kwargs.pop('type', 'K7')
        bhp = kwargs.pop('bhp', '750')
        self.engine = Engine(Type, bhp)
        super().__init__(**kwargs)

    def show(self):
        super().show()
        print('Fuel:', self.fuel)
        print('Transmission: ', self.trans)
        self.engine.show()


# c=Car(year=2018,model='S9',make='Telsa',trans='Auto',bhp=250)
# c.show()
class Electric_car(Vehicle):
    def __init__(self, **kwargs):
        self.battery = kwargs.pop('battery', 80)
        super().__init__(**kwargs)

    def show(self):
        super().show()
        print('Battery:', self.battery, 'KWH')


class Hybrid_car(Vehicle):
    def __init__(self, **kwargs):
        self.range = kwargs.pop('range', 450)
        super().__init__(**kwargs)

    def show(self):
        super().show()
        print('Range: ', self.range, 'KMS')


c1 = Hybrid_car(make='Telsa', seats=2, model='S9', bhp=450, range=500, Type='V8')
c1.show()
print('-' * 40)
c2 = Electric_car(name='Naveen', bhp=630, Type='G6')
c2.show()
