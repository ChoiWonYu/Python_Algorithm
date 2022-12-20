import sys
input=sys.stdin.readline
N=5
arr=[]
for i in range(5):arr.append(int(input()))
arr.sort()
print(int(sum(arr)//N),arr[2])