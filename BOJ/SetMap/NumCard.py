import sys
input=sys.stdin.readline

N=int(input())
C=list(map(int,input().split()))
SC=set(C)
M=int(input())
Q=list(map(int,input().split()))
SQ=set(Q)
result=SC.intersection(SQ)
for i in Q:
    if i in result:
        print(1,end=' ')
    else:print(0,end=' ')

