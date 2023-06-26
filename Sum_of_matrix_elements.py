n=int(input())
k=int(input())
s=0
for i in range(n):
    a=list(map(int,input().split()))
    p=sum(a)
    s=s+p
print(s)