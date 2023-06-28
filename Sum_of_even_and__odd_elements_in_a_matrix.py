n,m=map(int,input().split())
se=0
so=0
for i in range(n):
    l=list(map(int,input().split()))
    for j in l:
        if j%2==0:
            se=se+j
        else:
            so=so+j
print(se,end=' ')
print(so)