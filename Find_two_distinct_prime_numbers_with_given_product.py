n=int(input())
a=[2,3,5]
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
b=[]
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
c=[]
for i in b:
    k=prime(i)
    if k==2:
        c.append(i)
if len(c)<2:
    print("-1")
else:
    print(c[0],c[1])

    