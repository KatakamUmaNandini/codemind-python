n=int(input())
a=list(map(int,input().split()))
b=[]
p=1
while(1):
    if p>max(a):
        break
    b.append(p)
    p+=1
x=0
for i in b:
    if i not in a:
        print(i)
        x+=1
        break
if x==0:
    print(max(a)+1)