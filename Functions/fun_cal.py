def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
while True:
    print("Welcome to python functions")
    n1=int(input("enter a number"))
    n2=int(input("enter another number"))
    print("1:add, 2:sub, 3:mul, 4:div, 5:mod, 6:exit")
    ch=int(input("Please enter a number"))
    match ch:
        case 1:print(add(n1,n2))
        case 2:print(sub(n1,n2))
        case 3:print(mul(n1,n2))
        case 4:print(div(n1,n2))
        case 5:print(mod(n1,n2))
        case 6:exit