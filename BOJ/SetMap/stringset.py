import sys
input=sys.stdin.readline
N,M=(map(int,input().split()))
NS=set(input().strip() for _ in range(N))
MS=list(input().strip() for _ in range(M))
count=0
for i in MS:
    if i in NS:count+=1
print(count)