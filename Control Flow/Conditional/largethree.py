a=int(input("enter first no:"))
b=int(input("enter first no:"))
c=int(input("enter first no:"))
if a>b and a>c:
    print(f"{a} a is largest")
elif b>a and b>c:
    print(f"{b} b is largest")
else:
    print(f"{c} c is largest")