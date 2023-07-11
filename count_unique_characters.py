n=input()
c=[]
for i in n:
    if n.count(i)==1 and ord(i)>=97:
        c.append(i)
print(len(c))
