a,b,c=map(int,input().split())
if(a>50 and b>60 and c>100):
    print('10',end=" ")
elif a>50 and b>60:
    print('9',end=" ")
elif b>60 and c>100:
    print('8',end=" ")
elif a>50 and c>100:
    print('7',end=" ")
elif a>50 or b>60 or c>100:
    print('6',end=" ")
else:
    print('5',end=" ")