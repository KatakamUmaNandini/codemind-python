n=int(input())
a=[]
while n>0:
    t=n%10
    a.append(t)
    n=n//10
print(max(a))