n=int(input())
s=n*n
c=0
c1=0
while(n>0):
    t=n%10
    c=c+1
    k=s%10
    if(t==k):
        c1=c1+1
    n=n//10
    s=s//10
if c==c1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    