n=int(input())
p=0
u=n
while(n>0):
    a=n%10
    p=(p*10)+a
    n=n//10
if(p==u):
    print(True)
else:
    print(False)