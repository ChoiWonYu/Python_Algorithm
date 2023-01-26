import sys,itertools
input=sys.stdin.readline
N,M=map(int,input().split())
result=list(itertools.combinations([i for i in range(1,N+1)],M))
for i in result:
    for j in i:
        print(j,end=' ')
    print()