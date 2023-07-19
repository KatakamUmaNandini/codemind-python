n=int(input())
a=list(map(int,input().split()))
k=min(a)
for i in range(k,0,-1):
    c=0
    for j in a:
        if(j%i==0):
            c+=1
    if c==n:
        print(i)
        break