import sys
input=sys.stdin.readline
(nums,count)=map(int,input().split())
num=list(map(int,input().split()))
result=[0]
s=0
for i in num:
    s+=i
    result.append(s)
for _ in range(count):
    s,f=map(int,input().split())
    print(result[f]-result[s-1])
