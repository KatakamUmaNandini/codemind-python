n=int(input())
a=list(map(int,input().split()))
v=[]
for i in a:
    c=a.count(i)
    if(c==i and i not in v):
        v.append(i)
if(len(v)==0):
    print("-1")
else:
    print(min(v),end=' ')
    print(max(v))
