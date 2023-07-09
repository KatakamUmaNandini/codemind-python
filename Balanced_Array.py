t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for j in range(n):
        k=[]
        y=[]
        k=a[:j]
        y=a[j+1:]
        if(sum(k)==sum(y)):
            c+=1
            break
    if(c!=0):
        print("YES")
    else:
        print("NO")