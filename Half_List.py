n=int(input())
a=list(map(int,input().split()))
v=a[:n//2]
b=a[n//2:]
c=b[-1: :-1]
print(*c,end=' ')
print(*v)