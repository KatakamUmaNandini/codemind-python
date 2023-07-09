n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(n1):
    c.insert(b[i],a[i])
print(*c)