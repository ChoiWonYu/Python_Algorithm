import sys
input=sys.stdin.readline

c=int(input())
for i in range(c):
    n,m=map(int,input().split())
    a,b=1,1
    for i in range(m,m-n,-1):
        a*=i
    for j in range(n,1,-1):
        b*=j
    print(a//b)