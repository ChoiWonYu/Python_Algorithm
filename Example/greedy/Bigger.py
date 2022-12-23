import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
f=l[len(l)-1]
s=l[len(l)-2]
count=0
num=0
count=(M//(K+1))*K
count+=M%(K+1)
num+=count*f
num+=(M-count)*s
print(num)