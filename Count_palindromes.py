n=int(input())
a=list(map(int,input().split()))
def pal(n):
    q=n
    r=0
    while(n>0):
        t=n%10
        r=(r*10)+t
        n=n//10
    if r==q:
        return 1
    else:
        return 0
c=0
for i in a:
    p=pal(i)
    if p==1:
        c=c+1
print(c)