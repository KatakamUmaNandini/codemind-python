n=input()
p=list(n)
for i in p:
    if n.count(i)==1:
        print(n.index(i))
        break
else:
    print('-1')