n=input()
c=[]
for i in n:
    if i not in c and ord(i)>=97:
        c.append(i)
print(len(c))
