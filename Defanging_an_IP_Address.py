n=input()
for i in range(0,len(n)):
    if n[i]=='.':
        s=n.replace(".","[.]")
print(s)