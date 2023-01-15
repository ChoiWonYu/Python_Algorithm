import sys
input=sys.stdin.readline
a,b=map(int,input().split())
aa=a;bb=b
while b:
    a,b=b,a%b
print(a)
print(aa*bb//a)