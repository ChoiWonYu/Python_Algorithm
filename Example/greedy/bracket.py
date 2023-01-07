import sys
input=sys.stdin.readline
str=input().strip()
arr=str.split('-')
result=[]
for i in arr:
    result.append(sum(map(int,i.split('+'))))
print(result[0]-sum(result[1:]))