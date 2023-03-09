import sys
input=sys.stdin.readline

def getAction(o,l):
    act=[]
    n=[]
    for i in l:
        if o:
            while i>o[-1]:
                n.append(o.pop())
                act.append('+')
        if o and i==o[-1]:
            n.append(o.pop())
            act.append('+')
        if n and n[-1]!=i:
            return False
        n.pop()
        act.append('-')
    return act




n=int(input())
o=[i for i in range(n,0,-1)]
l=[]
for i in range(n):
    num=int(input())
    l.append(num)
act=getAction(o,l)
if act:
    for i in act:
        print(i)
else:
    print('NO')

