n=int(input())
a=list(map(int,input().split()))
d=set(a)
s=0
for i in d:
    if(i%2==0):
        s=s+i
print(s)