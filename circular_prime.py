def prime(u):
    c=0
    for i in range(1,u+1):
        if(u%i==0):
            c=c+1
    return c
n=int(input())
g=n
r=0
while n>0:
    t=n%10
    r=(r*10)+t
    n=n//10
h=prime(g)
j=prime(r)
if(h==2 and j==2):
    print('circular prime')
elif(h==2 and j!=2):
    print('prime but not a circular prime')
else:
    print('not prime')