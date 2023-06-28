n,m=map(int,input().split())
se=0
so=0
for i in range(1,n+1):
    l=list(map(int,input().split()))
    if i%2==0:
        se=se+sum(l)
    else:
        so=so+sum(l)
print(so,end=' ')
print(se)