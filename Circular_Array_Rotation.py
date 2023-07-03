n,k,q=map(int,input().split())
a=list(map(int,input().split()))
for j in range(k):
    a.insert(0,a[n-1])
    a.pop()
for i in range(q):
    m=int(input())
    print(a[m])
    