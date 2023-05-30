n=int(input())
c=0
for i in range(n):
    m=input()
    for j in m:
        if j.isdigit()==True:
            c=c+1
    if c==0:
        print('No')
    else:
        print('Yes')
    c=0