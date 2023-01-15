import sys
input=sys.stdin.readline
c=int(input())
for i in range(c):
    a,b=map(int,input().split())
    aa=a;bb=b
    while b:
        a,b=b,a%b
    print(aa*bb//a)

