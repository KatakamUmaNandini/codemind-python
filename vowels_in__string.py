n=input()
v=[]
b=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=='O' or i=='U':
        v.append(i)
for i in v:
    if i not in b:
        b.append(i)
print(*b)