n=int(input())
a=list(map(int,input().split()))
for i in a:
    r=0
    while i>0:
        t=i%10
        r=r*10+t
        i=i//10
    print(r,end=' ')
