import sys
input=sys.stdin.readline
N,M=map(int,input().split())
l=set(input().strip() for _ in range(N))
S=set(input().strip() for _ in range(M))
result=list(l.intersection(S))
print(len(result))
result.sort()
for i in result:
    print(i)