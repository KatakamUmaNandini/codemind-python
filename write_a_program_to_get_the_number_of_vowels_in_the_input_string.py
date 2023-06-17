n=input()
v=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        v.append(i)
if len(v)==0:
    print(0)
else:
    print(len(v))