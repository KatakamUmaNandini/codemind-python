t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(k):
        a.insert(0,a[n-1])
        a.pop()
    print(*a)