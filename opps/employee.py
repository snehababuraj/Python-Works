class Emp:
    company:str
    def __init__(self):
        self.company="Luminar"
    @property  #can add extra feature without changing the function definition
    def get_company_name(self):
        return self.company
    
    
obj=Emp()
print(obj.get_company_name)