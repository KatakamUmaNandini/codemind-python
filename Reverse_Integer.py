n=int(input())
def reverse(n):
    r=0
    while(n!=0):
        t=n%10
        r=(r*10)+t
        n=n//10
    return r
if(n>0):
    k=reverse(n)
    print(k)
else:
    k=reverse(-1*n)
    print('-',end='')
    print(k)