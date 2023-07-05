n=int(input())
for i in range(n):
    s1=input()
    s2="".join(reversed(s1))
    if(s1==s2):
        print("YES",end=' ')
        if(len(s1)%2==0):
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")