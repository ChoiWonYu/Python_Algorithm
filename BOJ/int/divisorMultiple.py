import sys
input=sys.stdin.readline
f,s=(1,1)
d='factor'
m='multiple'
n='neither'
while 1:
    f,s=map(int,input().split())
    if f==0 and s==0:
        break
    if f%s==0:
        print(m)
    elif s%f==0:
        print(d)
    else:
        print(n)
