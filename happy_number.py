n=int(input())
def add(n):
    s=0
    while(n!=0):
        t=n%10
        s=s+(t*t)
        n=n//10
    return s
def count(n):
    s=0
    while(n!=0):
        t=n%10
        s+=1
        n=n//10
    return s
while(1):
    n=add(n)
    c=count(n)
    if c==1:
        if n==1 or n==7:
            print(True)
        else:
            print(False)
        break