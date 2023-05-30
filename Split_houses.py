n=int(input())
p=input()
q=p.replace('.','B')
w=list(q)
c=0
for i in range(len(w)):
    if i==0:
        if w[i]=='H' and w[i+1]=='H':
            c=c+1
    else:
        if w[i]=='H' and w[i-1]=='H':
            c=c+1
if c==0:
    print("YES")
    print(q)
else:
    print("NO")