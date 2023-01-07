import sys
input=sys.stdin.readline
str=input().strip()
arr=str.split('-')
for i in range(len(arr)):
    arr[i]=list(map(int,arr[i].split('+')))
    arr[i]=sum(arr[i])
result=arr[0]
for i in range(1,len(arr)):
    result-=arr[i]
print(result)