n=input()
c=[]
for i in n:
    if n.count(i)==1 and ord(i)>=97:
        c.append(i)
if len(c)==0:
    print("-1")
else:
    print(c[0])
