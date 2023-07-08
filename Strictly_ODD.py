n=int(input())
a=list(map(int,input().split()))
c1=0
c2=0
for i in a:
    k=a.index(i)
    if(k%2==0 and i%2==0):
        c1+=1
    if(i%2==0):
        c2+=1
if(c1==c2):
    print(True)
else:
    print(False)