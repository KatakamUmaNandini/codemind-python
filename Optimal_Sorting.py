t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=sorted(a)
    if(k==a):
        c=0
    else:
        c=max(a)-min(a)
    print(c,end='
')