n=int(input())
b=list(map(int,input().split()))
x,y=map(int,input().split())
a=[]
for i in b:
    if i<x or i>y:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print(max(a))
