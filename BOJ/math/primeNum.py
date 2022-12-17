import math
d=123456*2
arr=[True for _ in range(d+1)]
arr[0]=False
arr[1]=False
for i in range(2,int(math.sqrt(d))+1):
    if arr[i]:
        j=2
        while i*j<=d:
            arr[i*j]=False
            j+=1
n=int(input())
while n!=0:
    print(arr[n+1:2*n+1].count(True))
    n=int(input())