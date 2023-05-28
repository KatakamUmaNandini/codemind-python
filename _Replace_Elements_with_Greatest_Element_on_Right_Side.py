n=int(input())
a=list(map(int,input().split()))
z=[]
for i in range(n-1):
    d=a[i+1:]
    m=max(d)
    z.append(m)
z.append(-1)
print(*z)