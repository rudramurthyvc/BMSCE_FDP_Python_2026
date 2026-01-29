def recu(n):
    if n == 1:
        return 1
    else:
        return n+recu(n-1)
val=recu(5)
print(val)

def fun(cnt):
    cnt=cnt+1
    print("hi")
    if cnt <15:
        fun(cnt)
    else:
        return
fun(10)