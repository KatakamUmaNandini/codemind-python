a,b=map(int,input().split())
for i in range(1,b):
    if a%i==0 and b%i==0:
        g=i
k=(a*b)//g
print(k)