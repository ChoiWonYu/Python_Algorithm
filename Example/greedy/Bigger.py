import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
f=l[len(l)-1]
s=l[len(l)-2]
count=0
num=0
while M!=0:
    if count==K:
        count=0
        num+=s
    else:
        count+=1
        num+=f
    M-=1
print(num)