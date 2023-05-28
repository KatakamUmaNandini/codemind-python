n=int(input())
a=list(map(int,input().split()))
p=1
d=[]
for i in a:
    p=p*i
for i in a:
    s=p//i
    d.append(s)
print(*d)