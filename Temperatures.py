n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if i==n-1:
        b.append(0)
    else:
        c=0
        for j in range(i+1,n):
            if a[j]>a[i]:
                b.append(j-i)
                c+=1
                break
        if c==0:
            b.append(0)
print(*b)