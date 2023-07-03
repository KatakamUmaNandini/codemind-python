n=int(input())
a=list(map(int,input().split()))
def dc(n):
    co=0
    while n>0:
        t=n%10
        co=co+1
        n=n//10
    return co
c=0
for i in a:
    k=dc(i)
    if k%2==0:
        c=c+1
print(c)