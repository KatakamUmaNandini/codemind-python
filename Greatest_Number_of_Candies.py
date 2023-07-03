n=int(input())
a=list(map(int,input().split()))
k=int(input())
m=max(a)
for i in a:
    if i+k>=m:
        print("True",end=' ')
    else:
        print("False",end=' ')