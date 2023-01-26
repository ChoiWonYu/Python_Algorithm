import itertools
import sys
from itertools import product
input=sys.stdin.readline
N,M=map(int,input().split())
for i in product([i for i in range(1,N+1)],repeat=M):
    print(*i)
