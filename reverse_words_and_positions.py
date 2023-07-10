n=input()
k=n.split(' ')
f=k[::-1]
for i in f:
    print(''.join(reversed(i)),end=' ')