import sys
input=sys.stdin.readline
N=int(input())
arr=[0]*8001
max=0
count=1
for i in range(N):
    n=int(input())
    arr[n+4000]+=1
    if arr[4000+n]>max:
        max=arr[4000+n]
        num=n
        count=1
    elif arr[4000+n]==max:
        count+=1
result=[]
for i in range(8001):
    if arr[i]>0:
        for _ in range(arr[i]):
            result.append(i-4000)
print(round(sum(result)/N))
print(result[N//2])
if count==1:
    print(num)
else:
    print(arr.index(max,arr.index(max)+1)-4000)
print(result[N-1]-result[0])
