#method overriding:method is same but different definition
class Grandparent:
    def m1(self):
        print("inside grandparent m1 method")

class Parent:
    def m1(self):
        print("inside parent m1 method")

class Child(Grandparent,Parent):
    pass
    #def m1(self):
        #print("inside child m1 method")
ch=Child()
ch.m1()
