n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    while i>0:
        t=i%10
        s=s+t
        i=i//10
print(s)