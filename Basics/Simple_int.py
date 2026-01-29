p=float(input("Enter principal:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time:"))
si=p*r*t/100
print(f"Simple interest is {si}")
print("Final amount payable is",p+si)
