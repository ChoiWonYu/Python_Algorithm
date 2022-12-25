import sys
input=sys.stdin.readline
N=int(input())
d={}
for _ in range(N):
    x,y=map(int, input().split())
    if y in d.keys():
        d[y].append(x)
    else:
        d[y]=[x]
for _ in d.keys():
    d[_].sort()
last=0;cnt=0
for i in sorted(d.keys()):
    for j in d[i]:
        if j>=last:
            cnt+=1
            last=i
# t=[tuple(map(int,input().split())) for _ in range(N)]
# t.sort()
# using=[]
# for x,y in t:
#     l=len(using)
#     if l==0:
#         using.append((x,y))
#     else:
#         if using[-1][1]>y:
#             while using and using[-1][1]>y:
#                 using.pop()
#             using.append((x,y))
#         elif using[-1][1]<=x:
#             using.append((x,y))
# print(len(using))


