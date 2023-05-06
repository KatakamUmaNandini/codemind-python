a=int(input())
b=list(map(int,input().split()))
c=0
d=0
e=list()
for i in b:
    if(i%2==0):
        c=c+1
    else:
        d=d+1
print(c,end=' ')
print(d)