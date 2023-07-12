n=int(input())
a=list(map(int,input().split()))
if n%2==0:
    b=a[:n//2]
    c=a[n//2:]
    d=c[::-1]
    for i in range(len(b)):
        print(b[i],end=' ')
        print(d[i],end=' ')
else:
    b=a[:n//2+1]
    c=a[n//2+1:]
    d=c[::-1]
    for i in range(len(c)):
        print(b[i],end=' ')
        print(d[i],end=' ')
    print(b[-1],end=' ')
    print("0")