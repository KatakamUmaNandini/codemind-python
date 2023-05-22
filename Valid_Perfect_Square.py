def fun(s):
    v=s**0.5
    g=int(v)
    if v==g:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    a=int(input())
    print(fun(a),end='
')