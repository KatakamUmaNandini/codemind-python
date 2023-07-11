n=input()
j=list(n)
c=j.count(' ')
for i in range(c):
    j.remove(' ')
print(min(j),j.count(min(j)),end=' ')
print(max(j),j.count(max(j)))