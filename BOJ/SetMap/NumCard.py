import sys
input=sys.stdin.readline

input()
C=set(map(int,input().split()))
input()
for i in map(int,input().split()):
    if i in C:print(1,end=' ')
    else:print(0, end=' ')

