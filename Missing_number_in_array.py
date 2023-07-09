t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for j in range(1,n+1):
        b.append(j)
    for k in b:
        if k not in a:
            print(k)
            break