class Calculator:
    def add(self):
        print("add")
class AdCalculator(Calculator):
    def sub(self):
        print("sub")
class SupCalculator(AdCalculator):
    def mul(self):
        print("mul")
a=SupCalculator()
a.add()
a.sub()
a.mul()