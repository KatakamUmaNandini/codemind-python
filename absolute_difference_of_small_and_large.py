n=input()
k=n.split(' ')
for i in k:
    print(ord(max(i))-ord(min(i)),end=' ')