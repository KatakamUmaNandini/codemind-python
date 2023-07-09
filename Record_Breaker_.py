t=int(input())
for i in range(1,t+1):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n):
        if j==0:
            if a[j]>a[j+1]:
                c+=1
        elif j==n-1:
            ac=0
            k=a[:j]
            for p in k:
                if(a[j]>p):
                    ac+=1
            if ac==len(k):
                c+=1
        else:
            af=0
            l=a[:j]
            for y in l:
                if a[j]>y:
                    af+=1
            if af==len(l) and a[j]>a[j+1]:
                c+=1
    print("Case #%d:"%i,c,end='
')