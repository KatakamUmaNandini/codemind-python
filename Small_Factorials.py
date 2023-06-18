n=int(input())
def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
for i in range(n):
    a=int(input())
    k=fact(a)
    print(k)