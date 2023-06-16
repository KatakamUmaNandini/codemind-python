n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
v=[]
for i in l:
    if i<a or i>b:
        v.append(i)
print(sum(v))