n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
v=[]
for i in range(n):
    if a[i] not in v and a[i] not in b:
        v.append(a[i])
for i in range(m):
    if b[i] not in v and b[i] not in a:
        v.append(b[i])
print(*v)