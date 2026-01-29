bal=int(input("enter the amount"))
if bal<=0:
    print("invalid amount")
else:
    print("valid amount")
    withd=int(input("amount to withdraw"))
    if withd <0 or withd> bal:
        print(f"amount should be greater than 0 and lessthan than {bal}")
    else:
        bal=bal-withd
        print("withdrawn successfully")
