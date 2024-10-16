class Food:
    name:str
    cuisine:str
    meal_type:str
    
    def __init__(self,name,cuisine,meal_type):
        self.name=name
        self.cuisine=cuisine
        self.meal_type=meal_type
    
    def display(self):
        print(self.name,self.cuisine,self.meal_type)

obj1=Food("ghee roast","indian","breakfast")
obj1.display()
obj2=Food("fried rice","chinese","lunch")
obj2.display()