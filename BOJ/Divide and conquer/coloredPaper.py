import sys

input=sys.stdin.readline
N=int(input())
arr=[]
result=[0,0]
def quad(data,startX,startY,size):
    startNum=data[startY][startX]
    flag=True
    for i in range(size):
        for j in range(size):
            if data[startY+i][startX+j]==startNum:
                continue
            else:
                flag=False
                break
        if not flag:break;
    if flag:result[startNum]+=1
    else:
        size//=2
        quad(data,startX,startY,size)
        quad(data,startX+size,startY,size)
        quad(data,startX,startY+size,size)
        quad(data,startX+size,startY+size,size)



for i in range(N):
    arr.append(list(map(int,input().split())))
quad(arr,0,0,N)
print(result[0])
print(result[1])