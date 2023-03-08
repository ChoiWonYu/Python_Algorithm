import sys
input=sys.stdin.readline
n=int(input())
def isVps(str):
    for i in str:
        if i=='(':
            s.append(i)
        else:
            if len(s)!=0:
                s.pop()
            else:
                return False
    if len(s)!=0:
        return False
    else:
        return True

for i in range(n):
    str=input().strip()
    s=[]
    if isVps(str):
        print('YES')
    else:
        print('NO')
