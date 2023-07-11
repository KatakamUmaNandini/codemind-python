n=input()
m=input()
k=n.lower()
b=m.lower()
p=k.split(' ')
q=b.split(' ')
for i in q:
    if i in p:
        print(i,end=' ')