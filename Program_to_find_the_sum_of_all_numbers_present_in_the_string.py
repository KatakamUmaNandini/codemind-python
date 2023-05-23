n=input()
s=0
for i in n:
    if i.isdigit()==True:
        v=int(i)
        s=s+v
print(s)