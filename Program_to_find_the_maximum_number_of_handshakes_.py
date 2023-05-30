def fact(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1
    return f
n=int(input())
a=fact(n)
b=fact(n-2)
c=a//(b*2)
print(c)