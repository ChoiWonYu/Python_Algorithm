data=1000
def isHan(n):
    arr=list(map(int,str(n)))
    if arr[0]-arr[1]==arr[1]-arr[2]:
        return True
    return False
num=int(input())
if num<111:
    if num>99:
        print(99)
        exit(0)
    else:
        print(num)
        exit(0)
else:
    arr = [False for _ in range(data + 1)]
    for i in range(111, data + 1):
        if isHan(i) == True:
            arr[i] = True
    count=99
    for i in range(111,num+1):
        if arr[i]==True:
            count+=1
    print(count)

