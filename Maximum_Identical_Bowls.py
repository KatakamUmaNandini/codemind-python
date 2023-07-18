n=int(input())
a=list(map(int,input().split()))
k=sum(a)
for i in range(n,0,-1):
    if k%i==0:
        print(i)
        break
