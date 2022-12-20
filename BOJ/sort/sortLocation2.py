import sys
input=sys.stdin.readline
N=int(input())
arr=[]
for _ in range(N):
    x,y=list(map(int,input().split()))[::-1]
    arr.append([x,y])
arr.sort()
for location in arr:
    x,y=location[::-1]
    print(x,y)