n1=int(input())
n2=int(input())
def bp(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    return c
i=n1+n2+1
while(1):
    k=bp(i)
    if k==2:
        print(i-(n1+n2))
        break
    i+=1