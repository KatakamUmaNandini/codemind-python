n=int(input())
y=n
w=[]
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
while(1):
    v=prime(n)
    if v==2:
        k=n
        break
    n=n+1
while(1):
    n=n-1
    c=prime(n)
    if c==2:
        p=n
        break
w=[]
w.append(k-y)
w.append(y-p)
print(min(w))