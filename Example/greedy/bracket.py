import sys
input=sys.stdin.readline
l=input().strip().split('+')
if len(l)!=1:
    for i in range(1,(len(l)-1)*2):print(i)

