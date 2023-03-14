import sys
from collections import deque

input=sys.stdin.readline
N,M=map(int,input().split())
d=deque([i for i in range(1,N+1)])
targetNum=list(map(int,input().split()))
result=0

while targetNum:
    if targetNum[0]==d[0]:
        targetNum.pop(0)
        d.popleft()
    else:
        if d.index(targetNum[0])>=len(d)/2:
            while d[0]!=targetNum[0]:
                d.rotate(1)
                result+=1
        else:
            while d[0]!=targetNum[0]:
                d.rotate(-1)
                result+=1
print(result)