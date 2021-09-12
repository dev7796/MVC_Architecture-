class Vehicles():
    def start(self):
        print("This is Vehicles")

class Aeroplane(Vehicles):
    def fly(self):
        print("This can Fly")
    def Fast(self):
        print("This is fast")

class Bus(Vehicles):
    def capacity(self):
        print("It has Capacity")
    def affordable(self):
        print("This is affordable")

class Bike(Vehicles):
    def engine(self):
        print("It has an Engine")


class AirBus(Aeroplane,Bus):
    def combined(self):
        print("This is an Airbus")
        self.fly()
        self.Fast()
        self.capacity()
        self.affordable()

class AirBike(AirBus,Bike):
    def combined(self):
        print("This is an AirBike")

a = AirBike()
a.combined()
a.fly()
a.capacity()
AirBus.combined(a)

'''Flow... Vehicles >>> Aeroplane  ---|
                    >>> Bus   ---      >>> Airbus ---|
                    >>> Bike        ---            >>> AirBike'''