class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def printname(self):
        print(self.make,self.model,self.year)
maruthi=Car("mariu",'honda',2020)
benz=Car("benz",'honda',2020)
maruthi.printname()
benz.printname()