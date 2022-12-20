import sys
input=sys.stdin.readline
N,k=map(int,input().split())
arr=list(sorted(map(int,input().split())))[::-1]
print(arr[k-1])