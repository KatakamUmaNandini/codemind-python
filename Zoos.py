n=input()
b=list(n)
cz=0
co=0
for i in b:
    if i=='z':
        cz=cz+1
    else:
        co=co+1
if 2*cz==co:
    print('Yes')
else:
    print('No')