class Animal:
    name:str
    animal_typ:str

    def __init__(self,name,animal_typ):
        self.name=name
        self.animal_typ=animal_typ
    def display(self):
        print(self.name,self.animal_typ)

class Lion(Animal):
    sound:str
    def __init__(self, name, animal_typ,sound):
        super().__init__(name, animal_typ)
        self.sound=sound

    def display(self):
        super().display()
        print(self.sound)

class Elephant(Animal):
    sound:str
    def __init__(self, name, animal_typ,sound):
        super().__init__(name, animal_typ)
        self.sound=sound

    def display(self):
        super().display()
        print(self.sound)


obj=Lion("Lion","carnivorus","roar")
obj.display()
obj1=Elephant("Elephant","herbivorus","roar")
obj1.display()

#method overriding:same method for parent class and child class but different definition