n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if a.count(i)==1:
        k.append(i)
if len(k)==0:
    print("-1")
else:
    print(max(k))