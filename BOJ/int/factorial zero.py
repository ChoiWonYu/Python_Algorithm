import sys
input=sys.stdin.readline
n=int(input())
result=1
for i in range(n,1,-1):
    result*=i
result=str(result)
count=0
for i in range(len(result)-1,0,-1):
    if result[i]!='0':break
    count+=1
print(count)