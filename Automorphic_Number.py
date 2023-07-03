n=int(input())
s=n*n
c=0
while n!=0:
    t=n%10
    v=s%10
    if t!=v:
        c+=1
    n=n//10
    s=s//10
if c==0:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")