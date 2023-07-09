t=int(input())
for i in range(t):
    n=int(input())
    c=0
    a=[]
    while(n!=0):
        t=n%10
        c+=1
        a.append(t)
        n=n//10
    b=[]
    h=min(a)
    l=max(a)
    for j in range(c):
        b.append(h)
        h+=1
    x=0
    for q in b:
        if q not in a:
            x+=1
    if x==0:
        print("YES")
    else:
        print("NO")