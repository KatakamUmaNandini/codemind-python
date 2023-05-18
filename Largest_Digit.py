n=int(input())
b=[]
while(n>0):
    a=n%10
    b.append(a)
    n=n//10
print(max(b))