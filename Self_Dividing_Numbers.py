a=int(input())
b=int(input())
for i in range(a,b+1):
    c1=0
    c2=0
    g=i
    while(i>0):
        t=i%10
        c1=c1+1
        if t==0:
            break
        else:
            if g%t==0:
                c2=c2+1
        i=i//10
    if c1==c2:
        print(g,end=' ')