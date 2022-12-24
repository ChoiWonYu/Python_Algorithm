import sys
input=sys.stdin.readline
N,sum=map(int,input().split())
coin=[int(input()) for _ in range(N)]
count=0

while sum>0 and coin:
    i=coin.pop()
    if i<=sum:
        count+=sum//i
        sum%=i

print(count)

