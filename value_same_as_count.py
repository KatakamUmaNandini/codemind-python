n=int(input())
a=list(map(int,input().split()))
v=[]
for i in a:
    k=a.count(i)
    if i==k and i not in v:
        v.append(i)
print(len(v))