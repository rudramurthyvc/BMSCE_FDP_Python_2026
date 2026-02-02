#Defn: A list is a ordered, mutable collection of items
# Properties: Ordered, Mutable, Allows Duplicates
li=[1,120.5,"a",'BMS'] #Syntax using []

li[1]=100

print(li[0:2])
print(li[-2])
#print(li)
li1=list(range(1,11,3))
for i in li1:
    print(i,end=" ")
li1.append("hello")
print(li1)
for i in range(4,10):
    li1.append(i)
print(li1)
li1.insert(2,"hello")
print(li1)
