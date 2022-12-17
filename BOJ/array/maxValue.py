import sys
N,M=(9,9)
input=sys.stdin.readline
arr=[list(map(int,input().split())) for _ in range(N)]
m=0
idx=[]
for i in range(N):
    if m<=max(arr[i]):
        m=max(arr[i])
        idx=[i+1,arr[i].index(m)+1]
print(m)
print(*idx)
