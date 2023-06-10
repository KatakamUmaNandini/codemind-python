n=int(input())
a=list(map(int,input().split()))
v=[]
for i in a:
    c=a.count(i)
    if(c==i and i not in v):
        v.append(i)
print(len(v))
