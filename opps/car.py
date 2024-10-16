class Vehicle:
    name:str
    brand:str

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def display_specs(self):
        print(self.name,self.brand)

class Car(Vehicle):
    transmission_type:str

    def __init__(self,name,brand,transmission):
        super().__init__(name,brand)
        self.transmission_type=transmission

    def display_specs(self):
        super().display_specs()
        print(self.transmission_type)



obj=Car("fronx","nexa","manuel")
obj.display_specs()