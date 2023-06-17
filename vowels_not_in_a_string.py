n=input()
v=[]
x=['a','e','i','o','u']
c=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v.append(i)
for i in x:
    if i not in v:
        c.append(i)
if len(c)==0:
    print("0")
else:
    print(*c)
        
    