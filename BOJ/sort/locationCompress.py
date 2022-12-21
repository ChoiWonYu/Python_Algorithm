import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
length=len(set(arr))
count=0
m=0
while count!=length:
    if count==0:
        m=min(arr)
        for i in range(n):
            arr[i]-=m
    else:
        m=max(arr)
        for i in range(n):
            if arr[i]>count-1 and arr[i]<m:
                m=arr[i]
        for i in range(n):
            if arr[i]>count:
                arr[i]-=m-count
    count+=1
print(arr)