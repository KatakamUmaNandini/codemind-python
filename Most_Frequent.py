n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=list(b)
m=[]
co=0
for i in c:
    for j in range(len(a)):
        if i==a[j]:
            co=co+1
    m.append(co)
    co=0
h=max(m)
d=m.index(h)
print(c[d])
