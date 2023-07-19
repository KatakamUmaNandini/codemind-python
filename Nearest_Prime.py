t=int(input())
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
for i in range(t):
    n=int(input())
    y=n
    while(1):
        v=prime(n)
        if v==2:
            k=n
            break
        n=n+1
    while(1):
        n=n-1
        p=prime(n)
        if p==2:
            h=n
            break
    if(k-y<y-h):
        print(k)
    else:
        print(h)