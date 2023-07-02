n=int(input())
a=list(map(int,input().split()))
c=0
ce=0
for i in range(n):
    if a[i]%2==0:
        ce=ce+1
    if a[i]%2==0 and i%2==0:
        c=c+1
if c==ce:
    print(True)
else:
    print(False)