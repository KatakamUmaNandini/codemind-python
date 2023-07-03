n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k):
    a.insert(n,a[0])
    a.pop(0)
print(*a)