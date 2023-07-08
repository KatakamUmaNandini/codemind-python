t=int(input())
for i in range(t):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n):
        f=[]
        g=[]
        k=a.index(a[j])
        f=a[:k]
        g=a[k+1:]
        if(sum(f)==sum(g)):
            y=j
            c+=1
            break
    if(c==0):
        print("-1",end='
')
    else:
        print(y,end='
')