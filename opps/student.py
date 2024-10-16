class Student:
    name:str
    course:str
    degree:str

    def set_student(self,name,course,degree):
        self.name=name
        self.course=course
        self.degree=degree

    def display(self):
        print(self.name,self.course,self.degree)


obj1=Student()
obj1.set_student("sneha","djgano","msc")
obj1.display()
obj2=Student()
obj2.set_student("sruthy","django","btech")
obj2.display()
obj3=Student()
obj3.set_student("basi","django","bca")
obj3.display()

