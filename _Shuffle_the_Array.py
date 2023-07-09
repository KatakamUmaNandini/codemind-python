n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=a[:k]
c=a[k:]
for i in range(k):
    print(b[i],c[i],end=' ')