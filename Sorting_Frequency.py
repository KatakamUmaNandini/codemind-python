n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    c.append(a.count(i))
d=list(set(c))
d.sort(reverse=True)
f=set(a)
for i in d:
    h=[]
    for j in f:
        if a.count(j)==i:
            h.append(j)
    print(*h,end=' ')
    