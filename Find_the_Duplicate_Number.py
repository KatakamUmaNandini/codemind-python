n=int(input())
a=list(map(int,input().split()))
for i in a:
    k=a.count(i)
    if k>1:
        print(i)
        break