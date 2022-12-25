import sys
input=sys.stdin.readline
N=int(input())
t=[tuple(map(int,input().split())) for _ in range(N)]
t.sort()
using=[]
for x,y in t:
    l=len(using)
    if l==0:
        using.append((x,y))
    else:
        if using[-1][1]>y:
            while using and using[-1][1]>y:
                using.pop()
            using.append((x,y))
        elif using[-1][1]<=x:
            using.append((x,y))
print(len(using))


