import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
for i in range(N):
    f = input().strip()
    isError=False
    size=int(input())
    flag=True
    if size==0:
        input()
        arr=[]
    else:
        arr=input().strip().replace('[','').replace(']','').split(',')
    d=deque(arr)
    for i in f:
        if i=='R':
            flag=not flag
        elif i=='D':
            if len(d)==0:
                isError=True
                break
            if flag:
                d.popleft()
            else:
                d.pop()
        else:
            continue
    if isError:
        print('error')
    else:
        if not flag:
            d.reverse()
        print("[" + ",".join(d) + "]")
        #리스트 바로 출력해서 계속 틀렸음;
