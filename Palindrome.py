n=int(input())
u=n
r=0
while n>0:
    t=n%10
    r=(r*10)+t
    n=n//10
if r==u:
    print(True)
else:
    print(False)