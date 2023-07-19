s=input()
sa=input()
c=s[::-1]
d=sa[::-1]
w=[]
t=[]
for i in s:
    w.append(i)
    if i=='#':
        w.pop()
        w.pop()
    
for i in sa:
    t.append(i)
    if i=='#':
        t.pop()
        t.pop()

if w==t:
    print("True")
else:
    print("False")