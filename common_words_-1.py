n=input()
m=input()
a=n.lower()
b=m.lower()
k=a.split(' ')
v=b.split(' ')
c=0
for i in v:
    if i in k:
        c+=1
print(c)