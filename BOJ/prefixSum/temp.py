import sys
input=sys.stdin.readline
num,count=map(int,input().split())
temp=list(map(int,input().split()))
result=[0]
s=0
max=-100000001
for i in temp:
    s+=i
    result.append(s)
for i in range(count,num+1):
    n=result[i]-result[i-count]
    if max<n:max=n
print(max)