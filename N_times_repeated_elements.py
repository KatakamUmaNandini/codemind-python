n=int(input())
a=list(map(int,input().split()))
k=int(input())
v=[]
for i in a:
    c=a.count(i)
    if(c==k and i not in v):
        v.append(i)
if(len(v)==0):
    print("-1")
else:
    print(*v)
