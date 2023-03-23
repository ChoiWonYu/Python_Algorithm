import sys

input = sys.stdin.readline

result = [0, 0, 0]


def tree(arr, startX, startY, size):
    flag = arr[startY][startX]
    if size==1:
        result[flag + 1] += 1
        return

    for i in range(size):
        for j in range(size):
            if arr[startY + i][startX + j] != flag:
                size //= 3
                tree(arr, startX, startY, size)
                tree(arr, startX + size, startY, size)
                tree(arr, startX + size*2, startY, size)

                tree(arr, startX, startY + size, size)
                tree(arr, startX, startY + size*2, size)

                tree(arr, startX+size, startY + size*2, size)
                tree(arr, startX+size*2, startY + size, size)

                tree(arr, startX + size, startY + size, size)
                tree(arr, startX + size*2, startY + size*2, size)
                return
    result[flag + 1] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

tree(arr,0,0,N)

for i in result:
    print(i)
