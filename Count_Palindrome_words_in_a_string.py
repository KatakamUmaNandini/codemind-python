n=input()
m=n.lower()
k=m.split(' ')
c=0
for i in k:
    l=i[::-1]
    if i==l:
        c+=1
print(c)