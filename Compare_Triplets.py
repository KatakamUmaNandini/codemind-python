a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
v=0
for i in range(0,3):
    if(a[i]>b[i]):
        c=c+1
    if a[i]<b[i]:
        v=v+1
print(c,end=' ')
print(v,end=' ')
    