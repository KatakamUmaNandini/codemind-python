n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
v=[]
for i in range(n):
   
    if a[i] in b and a[i] not in v:
        v.append(a[i])
print(*v)