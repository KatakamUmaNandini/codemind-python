n=int(input())
a=list(map(int,input().split()))
c=0
co=0
for i in a:
    if i==0:
        c=c+1
    else:
        co=co+1
for i in range(c):
    print('0',end=' ')
for i in range(co):
    print('1',end=' ')