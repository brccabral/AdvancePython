class Vehical:
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print('Driving')
    def stop(self):
        self.speed = 0
        print('Stopped')
    def display(self):
        print(f'Driving at {self.speed} speed')

class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing')
    def display(self):
        print(f'Freezing at {self.temp} temp')

class FreezerTruck(Freezer, Vehical):
    pass
class TruckFreezer(Vehical, Freezer):
    pass


class FreezerTruckFull(Freezer, Vehical):
    def display(self):
        print(f'Is a freezer: {issubclass(FreezerTruckFull, Freezer)}')
        print(f'Is a vehical: {issubclass(FreezerTruckFull, Vehical)}')
        # calling from super() will fail because
        # FreezerTruckFull inherits display() from Freezer
        # super(Vehical, self).display()
        
        # correct way
        Freezer.display(self)
        Vehical.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-30)
t.display() # display from Freezer
print('-'*20)

t = TruckFreezer()
t.drive(30)
t.freeze(-20)
t.display() # display from Vehical
print('-'*20)

t = FreezerTruckFull()
t.drive(20)
t.freeze(-50)
t.display() # display from FreezerTruckFull
print('-'*20)
