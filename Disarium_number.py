n=int(input())
u=n
r=n
s=0
c=0
while n>0:
    p=n%10
    c=c+1
    n=n//10
while u>0:
    t=u%10
    q=t**c
    c=c-1
    s=s+q
    u=u//10

if(s==r):
    print(True)
else:
    print(False)