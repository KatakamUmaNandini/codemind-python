n=int(input())
a=list(map(int,input().split()))
s=0
c=0
q=[]
p=a[-1::-1]
for i in p:
    s=s+i*(10**c)
    c=c+1
m=s+1
while m>0:
    b=m%10
    q.append(b)
    m=m//10
d=q[-1::-1]
print(*d)