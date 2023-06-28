n,m=map(int,input().split())
se=0
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    se=se+sum(l)
    a.append(se)
    se=0
print(max(a))