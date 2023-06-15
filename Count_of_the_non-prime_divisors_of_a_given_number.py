n=int(input())
v=[]
def prime(p):
    c=0
    for i in range(1,p+1):
        if(p%i==0):
            c=c+1
    return c
co=0
for i in range(1,n+1):
    if n%i==0:
        v.append(i)
for i in v:
    k=prime(i)
    if(k!=2):
        co=co+1
print(co)