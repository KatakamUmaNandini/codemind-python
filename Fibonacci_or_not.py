n=int(input())
a=0
b=1
k=[]
i=1
while(i<=n):
    k.append(a)
    c=a+b
    a=b
    b=c
    i=i+1
if n in k:
    print(True)
else:
    print(False)
    