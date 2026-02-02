class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print(self.name)
        print(self.age)
s1=Student(name="Harsha",age=10)
s1.printname()