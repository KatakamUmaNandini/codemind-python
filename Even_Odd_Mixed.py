n=int(input())
v=[]
co=0
ce=0
while(n>0):
    t=n%10
    v.append(t)
    n=n//10
for i in v:
    if(i%2==0):
        ce=ce+1
    else:
        co=co+1
if ce==len(v):
    print("Even")
elif co==len(v):
    print("Odd")
else:
    print("Mixed")