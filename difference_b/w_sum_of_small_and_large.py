n=input()
k=n.split(' ')
s=0
s1=0
for i in k:
    s=s+ord(max(i))
    s1=s1+ord(min(i))
print(s-s1)