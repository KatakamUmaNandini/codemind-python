n=int(input())
a=0
b=1
h=[]
while(1):
    if a>n:
        break
    else:
        h.append(a)
        c=a+b
        a=b
        b=c
if n in h:
    print(True)
else:
    print(False)