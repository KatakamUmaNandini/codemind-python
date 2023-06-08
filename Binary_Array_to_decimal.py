n=int(input())
a=list(map(int,input().split()))
s=0
b=a[::-1]
for i in range(n):
    if(b[i]==1):
        s=s+(2**i)
print(s)
    