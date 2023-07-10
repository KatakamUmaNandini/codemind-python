n=int(input())
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
k=prime(n)
if k!=2:
    print("Not Mega Prime")
else:
    c=0
    co=0
    while(n!=0):
        t=n%10
        v=prime(t)
        if v==2:
            c+=1
        co+=1
        n=n//10
    if c==co:
        print("Mega Prime")
    else:
        print("Not Mega Prime")