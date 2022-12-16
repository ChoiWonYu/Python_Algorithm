import sys
n=int(input())
"""
for i in range(n):
    ox=list(map(str,input()))
    score=0
    cum=0
    for i in ox:
        if i=='O':
            cum+=1
            score+=cum
        else:
            cum=0
    print(score)
"""
s=0
for _ in range(n):
    arr=sys.stdin.readline().rstrip().split('X')
    print(arr)
    for i in range(len(arr)):
        s+=sum(range(1,len(arr[i])+1))
    print(s)
    s=0


