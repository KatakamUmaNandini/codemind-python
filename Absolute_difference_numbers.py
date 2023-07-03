n,u=map(int,input().split())
m=n
r=0
k=u
f=0
for i in range(u):
    t=n%10
    r=r+(10**f)*t
    f+=1
    n=n//10
rev=0
while m>0:
    h=m%10
    rev=(rev*10)+h
    m=m//10
a=0
for i in range(k):
    p=rev%10
    a=a+(10**(k-1))*p
    k=k-1
    rev=rev//10

if r>a:
    q=r-a
else:
    q=a-r
print(q)
    
