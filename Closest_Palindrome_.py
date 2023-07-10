n=int(input())
def pal(n):
    h=n
    r=0
    while(n!=0):
        t=n%10
        r=(r*10)+t
        n=n//10
    if r==h:
        return 1
    else:
        return 0
i=n+1
while(1):
    k=pal(i)
    if k==1:
        p=i
        break
    i+=1
j=n-1
while(1):
    h=pal(j)
    if h==1:
        u=j
        break
    j=j-1
if n-u<p-n:
    print(u)
elif n-u>p-n:
    print(p)
else:
    print(u,end=' ')
    print(p)