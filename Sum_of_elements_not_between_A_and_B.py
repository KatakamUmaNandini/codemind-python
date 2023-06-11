n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in m:
    if i<a or i>b:
        s=s+i
print(s)