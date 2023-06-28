n=int(input())
x=64
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(x+i),end=' ')
    print()