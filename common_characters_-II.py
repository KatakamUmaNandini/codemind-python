n=input()
m=input()
k=n.lower()
b=m.lower()
c=[]
for i in b:
    if i in k and i not in c and i!=' ':
        c.append(i)
print(len(c))