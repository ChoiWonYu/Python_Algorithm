import sys
from itertools import combinations,product
input=sys.stdin.readline
N=int(input())
result=list(combinations(range(N*N),N))
for i in result:
    print(i)