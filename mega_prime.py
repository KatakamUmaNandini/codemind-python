n=int(input())
c=0
l=[]
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if(c!=2):
    print("Not Mega Prime")
else:
    count=0
    while n>0:
        t=n%10
        l.append(t)
        n=n//10
    for i in l:
        co=0
        for j in range(1,i+1):
            if i%j==0:
                co=co+1
        if(co==2):
            count=count+1
    if len(l)==count:
        print("Mega Prime")
    else:
        print("Not Mega Prime")