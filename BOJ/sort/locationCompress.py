import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
sArr=list(sorted(set(arr)))
dict={sArr[i]:i for i in range(len(sArr))}
for i in arr:
    print(dict[i], end=' ')