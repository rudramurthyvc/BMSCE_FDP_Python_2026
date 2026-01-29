size = int(input("enter the no of rows"))
for i in range(size):
    for j in range(size - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()


for i in range(size-2,-1,-1):
    for j in range(size - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
