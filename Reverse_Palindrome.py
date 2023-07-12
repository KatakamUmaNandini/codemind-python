n=int(input())
def reverse(n):
    r=0
    while(n!=0):
        t=n%10
        r=(r*10)+t
        n=n//10
    return r
def pal(n):
    m=n
    r=0
    while(n!=0):
        t=n%10
        r=(r*10)+t
        n=n//10
    if r==m:
        return 1
    else:
        return 0
while(1):
    n=n+reverse(n)
    if pal(n)==1:
        print(n)
        break
    