n=int(input())
x=0
for i in range(n):
    s=input()
    for j in s:
        a.append(j)
    if(s[0]=="+"):
        x+=1
    if(s[0]=="-"):
        x-=1
    if(s[-1]=="+"):
        x+=1
    if(s[-1]=="-"):
        x-=1
print(x)