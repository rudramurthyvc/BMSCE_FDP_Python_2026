class Mom:
    def cook(self):
        print("cook Mom")
class Dad:
    def sleep(self):
        print("sleep")
    def cook(self):
        print("cook Dad")
class Child(Dad,Mom):
    def study(self):
        print("study")
c=Child()
c.cook()
c.sleep()
c.study()