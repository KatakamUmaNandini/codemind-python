n=int(input())
s=n*n
r=0
rev=0
while n>0:
    t=n%10
    r=(r*10)+t
    n=n//10
sq=r*r
while sq>0:
    f=sq%10
    rev=(rev*10)+f
    sq=sq//10
if rev==s:
    print(True)
else:
    print(False)