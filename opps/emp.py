class Employee:
    emp_code:str
    name:str
    dept_name:str
    salary:int

    def __init__(self,emp_code,name,dept_name,salary):
        self.emp_code=emp_code
        self.name=name
        self.dept_name=dept_name
        self.salary=salary
    def display(self):
        print(self.emp_code,self.name,self.dept_name,self.salary)

#obj1=Employee()
#obj1.set_employee("E123","vijay","hr",45000)

obj1=Employee("E123","vijay","hr",45000)
obj1.display()
#obj2=Employee()
#bj2.set_employee("E124","vipin","it",47000)
#obj2.display()

#constructor:for initializing instance variable
# name always __init__(self,)
#constructor is a special method inside class
#constructore invoked during object creation

