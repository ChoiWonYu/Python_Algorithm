import sys
input=sys.stdin.readline
import math

def isIn(r,a,b):
    if r>math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2):return True
    else: return False

st=int(input())
for i in range(st):
    result=0
    arr=list(map(int,input().split()))
    start=[arr[0],arr[1]]
    end=[arr[2],arr[3]]

    count=int(input())
    for i in range(count):
        arr=list(map(int,input().split()))
        loc=[arr[0],arr[1]]
        r=arr[2]
        if isIn(r,loc,start) or isIn(r,loc,end):result+=1
        if isIn(r,loc,start) and isIn(r,loc,end):result-=1
    print(result)

