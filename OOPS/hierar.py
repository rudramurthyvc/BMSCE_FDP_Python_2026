class Calculator:
    def add(self):
        print("add")
class AdCalculator(Calculator):
    def sub(self):
        print("sub")
class SupCalculator(Calculator):
    def mul(self):
        print("mul")
a=SupCalculator()
b=AdCalculator()
b.add()
b.sub()
a.add()
a.mul()