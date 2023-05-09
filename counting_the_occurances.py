u=input()
n=input()
c=0
for i in u:
    if i==n:
        c=c+1
if c==0:
    print("-1")
else:
    print(c)