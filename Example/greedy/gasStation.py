import sys
input=sys.stdin.readline
city=int(input())
dist=list(map(int,input().split()))
price=list(map(int,input().split()))
result=0
min=price[0]
for i in range(len(dist)):
    if min>price[i]:min=price[i]
    result+=min*dist[i]

print(result)
