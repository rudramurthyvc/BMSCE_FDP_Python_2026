n=int(input("enter a no:"))
n1=0
n2=1
sum=0
print(n1,end=" ")
print(n2,end=" ")
for i in range(2,n+1):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum,end=" ")
