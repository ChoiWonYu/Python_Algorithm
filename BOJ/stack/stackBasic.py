import sys
input=sys.stdin.readline
stack=[]
top=0
n=int(input())
for i in range(n):
    arr=list(map(str,input().split()))
    if(len(arr)==2):
        stack.append(arr[1])
        top+=1
    else:
        act=arr[0]
        if act=='pop':
            if top==0:
                print(-1)
                continue
            print(stack.pop(top-1))
            top-=1
        elif act=='size':
            print(top)
        elif act=='empty':
            print(int(top==0))
        else:
            if top==0:
                print(-1)
                continue
            print(stack[top-1])
