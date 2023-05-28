n=int(input())
a=list(map(int,input().split()))
k=int(input())
if k not in a:
    print('-1')
else:
    print(a.index(k))