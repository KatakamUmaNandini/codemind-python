n=int(input())
p=1
s=0
while n>0:
    t=n%10
    p=p*t
    s=s+t
    n=n//10

if p==s:
    print('Spy Number')
else:
    print('Not Spy Number')

