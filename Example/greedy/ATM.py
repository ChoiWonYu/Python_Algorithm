import sys
input=sys.stdin.readline
N=int(input())
l=sorted(list(map(int, input().split())))
s=0
for i in range(N):
    s+=l[i]*(N-i)
print(s)