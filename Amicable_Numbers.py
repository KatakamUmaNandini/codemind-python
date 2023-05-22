a=int(input())
b=int(input())
c=a
d=b
def fun(e):
    s=0
    for i in range(1,e):
        if(e%i==0):
            s=s+i
    return s
        
q=fun(a)
z=fun(b)
if q==d and z==c:
    print('Amicable')
else:
    print('Not Amicable')
