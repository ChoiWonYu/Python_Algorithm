import sys
from collections import deque

input=sys.stdin.readline
N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

print(arr)