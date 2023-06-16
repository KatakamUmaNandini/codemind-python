n=int(input())
a=list(map(int,input().split()))
v=[]
for i in range(0,n-1,2):
    for j in range(a[i+1]):
        v.append(a[i])
print(*v)

