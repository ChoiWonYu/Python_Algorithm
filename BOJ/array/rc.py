import sys
input=sys.stdin.readline
a,b=map(int,input().split())
# aArr=[[]for _ in range(a)]
# bArr=[[]for _ in range(a)]
# rArr=[[]for _ in range(a)]
# for i in range(a):
#     aArr[i]=(list(map(int,input().split())))
#     rArr[i]=aArr[i]
# for i in range(a):
#     bArr[i]=(list(map(int,input().split())))
# for i in range(a):
#     for j in range(b):
#         rArr[i][j]=aArr[i][j]+bArr[i][j]
#         print(rArr[i][j],end=' ')
#     print()
aArr=[list(map(int,input().split())) for _ in range(a)]
bArr=[list(map(int,input().split())) for _ in range(a)]
for i,j in zip(aArr,bArr):
    print(*[x+y for x,y in zip(i,j)])