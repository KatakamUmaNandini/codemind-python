n=int(input())
q=n
v=[]
l=[]
def fact(p):
    f=1
    for i in range(1,p+1):
        f=f*i
    return f
while(n>0):
    t=n%10
    v.append(t)
    n=n//10
for i in v:
    k=fact(i)
    l.append(k)
if sum(l)==q:
    print("The number %d is a strong number"%q)
else:
    print("The number %d is not a strong number"%q)