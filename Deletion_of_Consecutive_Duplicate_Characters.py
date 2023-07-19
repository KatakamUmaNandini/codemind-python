t=int(input())
for i in range(t):
    n=input()
    c=0
    for j in range(len(n)-1):
        if n[j]==n[j+1]:
            c+=1
    print(c)