n=input()
k=n.split(' ')
b=min(k[-1])
if chr(ord(b)+32) in k[-1]:
    print(chr(ord(b)+32))
else:
    print(b)