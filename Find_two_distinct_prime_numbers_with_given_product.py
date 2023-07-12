n=int(input())
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
b=[]
c=[]
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
for i in b:
    if prime(i)==2:
        c.append(i)
if len(c)<2:
    print("-1")
else:
    print(*c)