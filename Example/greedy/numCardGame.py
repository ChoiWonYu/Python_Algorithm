import sys
input=sys.stdin.readline
r,c=map(int,input().split())
l=[]
m=[]
for i in range(r):
    newList=list(map(int,input().split()))
    l.append(newList)
    m.append(min(newList))
print(max(m))