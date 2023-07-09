t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(n//2):
        p=max(a)
        w=min(a)
        b.append(p)
        b.append(w)
        a.pop(a.index(p))
        a.pop(a.index(w))
        if(len(a)==1):
            b.append(a[0])
    print(*b)