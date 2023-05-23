n=int(input())
b=[]
c=0
for i in range(n):
    a=int(input())
    b.append(a)
t=int(input())
for i in b:
    if(i>t):
        c=c+1
print(n+c)