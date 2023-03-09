import sys
from collections import deque

input=sys.stdin.readline
q=deque()
n=int(input())

for i in range(n):
    s=list(input().split())
    act=s[0]
    if act=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif act=='back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif act=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif act=='size':
        print(len(q))
    elif act=='pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    else:
        q.append(s[1])
