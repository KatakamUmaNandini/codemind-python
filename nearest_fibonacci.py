n=int(input())
a=0
b=1
while(1):
    if n>a and n<b:
        h=a
        j=b
        break
    c=a+b
    a=b
    b=c
if n-h<j-n:
    print(h)
elif n-h>j-n:
    print(j)
else:
    print(h,end=' ')
    print(j)