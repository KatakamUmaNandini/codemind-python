n,m=map(int,input().split())
s=0
for i in range(n):
    l=list(map(int,input().split()))
    s=s+sum(l)
print(s)