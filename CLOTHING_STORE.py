n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
v=[]
c=0
for i in b:
    k=a.count(i)
    v.append(k)
for i in v:
    if i%2==0:
        c=c+(i//2)
    elif i==1:
        c=c+0
    else:
        c=c+((i//2))
print(c)