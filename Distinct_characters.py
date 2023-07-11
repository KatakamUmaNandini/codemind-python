n=input()
c=[]
for i in n:
    if i not in c and ord(i)>=97:
        c.append(i)
c.sort()
for i in c:
    print(i,end='')
