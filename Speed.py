t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print("1")
    else:
        c=0
        c1=0
        for i in range(n):
            if i==0:
                continue
            else:
                k=a[:i]
                for j in k:
                    if a[i]<j:
                        c=c+1
                if c==len(k):
                    c1=c1+1
                c=0
        print(c1+1)
                
            
            