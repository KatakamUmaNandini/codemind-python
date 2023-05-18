n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
avg=s//n
if avg in a:
    print(True)
else:
    print(False)