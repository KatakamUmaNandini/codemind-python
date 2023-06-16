n=int(input())
a=list(map(int,input().split()))
v=[]
for i in a:
    k=a.count(i)
    if i==k and i not in v:
        v.append(i)
if len(v)==0:
    print("-1")
else:
    print(*v)