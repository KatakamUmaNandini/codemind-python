t=int(input())
def pal(n):
    m=n
    r=0
    while n>0:
        t=n%10
        r=(r*10)+t
        n=n//10
    if r==m:
        return 1
    else:
        return 0
for i in range(t):
    n=int(input())
    k=pal(n)
    if k==1:
        print(True)
    else:
        print(False)