n=int(input())
u=n
s=n*n
su=0
while s!=0:
    t=s%10
    su=su+t
    s=s//10
if u==su:
    print('Neon Number')
else:
    print('Not Neon Number')