class Grandparnt():
    def m1(self):
        print("grand parent m1 method")
class Parent(Grandparnt):
    def m2(self):
        print("parent m2 method")
class Child(Parent,Grandparnt):
    def m3(self):
        print("child m3 method")

ch=Parent()
ch.m2()
ch.m3()
ch.m1()
