import sys

input=sys.stdin.readline
result=[]
def quad(arr,data,startX,startY,size):
    flag=data[startY][startX]
    if size==1:
        arr.append(flag)
        return
    for i in range(size):
        for j in range(size):
            if data[startY+i][startX+j]!=flag:
                pArr=[]
                arr.append(pArr)
                size//=2
                quad(pArr,data,startX,startY,size)
                quad(pArr, data, startX+size, startY, size)
                quad(pArr, data, startX, startY+size, size)
                quad(pArr, data, startX+size, startY+size, size)
                return
    arr.append(flag)

def Print(arr):
    if type(arr) is not list:
        print(arr,end='')
        return
    print('(',end='')
    for i in arr:
        if type(i) is list:
            Print(i)
        else:
            print(i,end='')
    print(')',end='')
    return



N=int(input())

arr=[list(map(int,input().rstrip())) for _ in range(N)]
quad(result,arr,0,0,N)
Print(result[0])
