n=input()
k=n.split(' ')
b=[]
for i in k:
    b.append(len(i))
print(max(b))