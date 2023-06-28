a=input()
l=[]
for i in a:
    if int(i)%2!=0:
        l.append(int(i)*int(i))
for i in l:
    print(i,end='')