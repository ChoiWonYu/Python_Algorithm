import sys

input=sys.stdin.readline
N=int(input())
arr=[]
result=[0,0]
def quad(data,startX,startY,size):
    flag=data[startY][startX]
    if size==1:
        result[flag]+=1
        return

    for i in range(size):
        for j in range(size):
            if data[startY+i][startX+j]!=flag:
                size //= 2
                quad(data, startX, startY, size)
                quad(data, startX + size, startY, size)
                quad(data, startX, startY + size, size)
                quad(data, startX + size, startY + size, size)
                return
    result[flag]+=1

for i in range(N):
    arr.append(list(map(int,input().split())))
quad(arr,0,0,N)
print(result[0])
print(result[1])