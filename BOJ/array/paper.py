import sys
N=100
input=sys.stdin.readline
arr=[[0 for _ in range(N+1)]for _ in range(N+1)]
n=int(input())
count=0
for _ in range(n):
    r, c = map(int, input().split())
    for i in range(r,r+10):
        for j in range(c,c+10):
            arr[i][j]+=1
            if arr[i][j]>=2:continue
            else:count+=1
print(count)
