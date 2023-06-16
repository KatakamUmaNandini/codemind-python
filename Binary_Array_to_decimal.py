n=int(input())
a=list(map(int,input().split()))
c=0
s=0
b=a[::-1]
for i in b:
    k=i*(2**c)
    c=c+1
    s=s+k
print(s)