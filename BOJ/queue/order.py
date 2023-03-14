import sys
from collections import deque

input=sys.stdin.readline
d=deque()
N=int(input())
for i in range(N):
    I=input().split()
    if I[0]=='push_front':
        d.appendleft(I[1])
    elif I[0]=='push_back':
        d.append(I[1])
    elif I[0]=='pop_front':
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())
    elif I[0]=='pop_back':
        if len(d)==0:
            print(-1)
        else:
            print(d.pop())
    elif I[0]=='size':
        print(len(d))
    elif I[0]=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif I[0]=='front':
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
    else:
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])
