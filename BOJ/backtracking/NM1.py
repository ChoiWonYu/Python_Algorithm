import sys
import itertools

input=sys.stdin.readline
N,M=map(int,input().split())
l=[i for i in range(1,N+1)]
result=itertools.permutations(l,M);
for i in list(result):
    for j in range(len(i)):
        print(i[j],end=' ')
    print()
