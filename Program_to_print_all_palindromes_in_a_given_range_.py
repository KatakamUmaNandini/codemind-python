a=int(input())
b=int(input())
def pal(n):
    r=0
    while(n>0):
        y=n%10
        r=(r*10)+y
        n=n//10
    return r
for i in range(a,b+1):
    k=pal(i)
    if k==i:
        print(i,end=' ')