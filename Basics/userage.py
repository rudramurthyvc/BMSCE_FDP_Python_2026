name=input("Enter your name:")
byear = int(input("Enter your birth year:"))
cyear=int(input("Enter current year:"))
age = cyear - byear
# print(type(age))
print(name + " You are "+ str(age) + " years old")
print(name,"You are",age,"years old")
print(f"{name} You are {age} years old")
print("{} You are {} years old".format(name,age))
