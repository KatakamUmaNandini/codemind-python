n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if i==0:
        x=a[n-1]
        y=a[i+1]
    if i==n-1:
        y=a[0]
        x=a[i-1]
    else:
        x=a[i-1]
        y=a[i+1]
    if x%2!=0 and y%2==0:
        c=c+1
    if x%2==0  and y%2!=0:
        c=c+1
print(c)