def name(*n):
    print(*n)
    print(n[0])
def hi(**n):
    print(n["a"])
name("Hello","all","Good","day")
hi(a=1,b=2,c=3)