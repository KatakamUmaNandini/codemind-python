n=input()
c=0
for i in n:
    if i.isalpha()==False and i.isdigit()==False and i!=' ':
        c+=1
print(c)