n=input()
v=[]
x=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v.append(i)
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        x.append(i)
g=list(set(v))
h=list(set(x))
if len(g)==5 or len(h)==5:
    print(True)
else:
    print(False)
        
    