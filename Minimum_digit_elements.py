n=int(input())
a=list(map(int,input().split()))
c=0
co=0
v=[]
for i in a:
    while i>0:
        t=i%10
        c=c+1
        i=i//10
    v.append(c)
    c=0
k=min(v)
for i in a:
    while i>0:
        t=i%10
        c=c+1
        i=i//10
    if c==k:
        co=co+1
    c=0
print(co)
