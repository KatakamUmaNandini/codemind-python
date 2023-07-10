s=input()
k=s.split(' ')
b=[]
for i in k:
    b.append(len(i))
print(min(b))