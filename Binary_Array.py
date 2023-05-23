n=int(input())
co=0
a=list(map(int,input().split()))
for i in a:
    if i==1 or i==0:
        co=co+1
if(co==n):
    print("True")
else:
    print("False")