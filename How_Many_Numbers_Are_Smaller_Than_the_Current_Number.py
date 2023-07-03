n=int(input())
a=list(map(int,input().split()))
c=0
for k in a: 
    for j in range(n):
        if j!=a.index(k) and a[j]<k:
            c=c+1
    print(c,end=' ')
    c=0
