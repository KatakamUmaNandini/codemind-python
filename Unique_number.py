n=int(input())
a=[]
while n>0:
    t=n%10
    a.append(t)
    n=n//10
b=set(a)
if len(a)==len(b):
    print('Unique Number')
else:
    print('Not Unique Number')
