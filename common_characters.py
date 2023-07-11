n=input()
m=input()
k=n.lower()
b=m.lower()
c=[]
for i in b:
    if i in k and i not in c and i!=' ' :
        c.append(i)
c.sort()
if len(c)==0:
    print("-1")
else:
    for i in c:
        print(i,end='')