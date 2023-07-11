n=input()
m=n.lower()
k=m.split(' ')
x=[]
c=0
for i in m:
    c=0
    for j in k:
        if i in j:
            c+=1
    if c==len(k):
        x.append(i)
if len(x)==0:
    print("-1")
else:
    x.sort()
    print(x[0])
 
