n=int(input())
a=list(map(int,input().split()))
b=a[:n//2]
c=a[n//2:]
m=sum(b)
s=sum(c)
if m>s:
    print(m-s)
else:
    print(s-m)
