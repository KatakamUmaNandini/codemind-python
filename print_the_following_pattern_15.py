n=int(input())
x=64
for i in range(n,0,-1):
    for j in range(i):
        print(chr(x+i),end=' ')
    print()