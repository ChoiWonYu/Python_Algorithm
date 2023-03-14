import sys
from collections import deque

input=sys.stdin.readline
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    arr=deque(map(int,input().split()))
    s=0
    c=1
    while 1:
        if max(arr)==arr[0]:
            if s%N==M:
                print(c)
                break
            else:
                arr[0]=0
                arr.rotate(-1)
                c+=1
        else:
            arr.rotate(-1)
        s+=1

