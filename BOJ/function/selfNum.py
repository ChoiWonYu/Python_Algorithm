data=10000
def makeSelfNum(n:int)->int:
    sum=n
    while n!=0:
        sum+=n%10
        n//=10
    return sum
arr=[True for _ in range(data+1)]
for i in range(1,data+1):
    if makeSelfNum(i)<=data:
        arr[makeSelfNum(i)] = False
for i in range(1,data+1):
    if arr[i]==True:
        print(i)