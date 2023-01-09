import sys
input=sys.stdin.readline
N,M=map(int,input().split())
pl=list(input().strip() for i in range(N))

print('\n'.join(map(lambda x:str(pl.index(x)+1) if x.isalpha() else pl[int(x)-1],[input().strip() for _ in range(M)])))