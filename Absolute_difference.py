n=int(input())
a=list(map(int,input().split()))
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return 1
    else:
        return 0
e=[]
d=[]
for i in a:
    k=prime(i)
    if k==1:
        e.append(i)
    else:
        d.append(i)
pp=1
pn=1
for i in e:
    pp=pp*i
for i in d:
    pn=pn*i
if pp>pn:
    y=pp-pn
else:
    y=pn-pp
print(y)
    