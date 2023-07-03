n=int(input())
a=list(map(int,input().split()))
for i in a:
    k=a.count(i)
    if k>(n//2):
        print(i)
        break