import sys
input=sys.stdin.readline
N=int(input())
l=sorted(list(map(int, input().split())))
s=0
for idx,i in enumerate(l):
    s+=i
    l[idx]=s
print(sum(l))

