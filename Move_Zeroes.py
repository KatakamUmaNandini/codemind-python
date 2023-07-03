n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==0:
        c=c+1
for i in range(c):
    a.remove(0)
    a.insert(n-1,0)
print(*a)