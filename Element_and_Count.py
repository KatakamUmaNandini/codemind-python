n=int(input())
a=list(map(int,input().split()))
p=[]
for i in a:
    if i not in p:
        p.append(i)
for i in p:
    k=a.count(i)
    print(i,k,end=' ')
    