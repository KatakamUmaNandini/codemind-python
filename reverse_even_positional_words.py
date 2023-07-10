n=input()
k=n.split(' ')
for i in range(len(k)):
    if i%2==0:
        print(''.join(reversed(k[i])),end=' ')
    else:
        print(k[i],end=' ')