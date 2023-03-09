import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
q=deque([i for i in range(1,n+1)])
l=[]
while q:
    q.rotate(-m+1)
    l.append(q.popleft())
print('<',end="")
print(', '.join(map(str,l)),end="")
print('>')