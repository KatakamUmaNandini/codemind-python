n=input()
k=n.split(' ')
a="aeiouAEIOU"
for i in k:
    c=0
    for j in i:
        if j in a:
            c+=1
    print(c,end=' ')