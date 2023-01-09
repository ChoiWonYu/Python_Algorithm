import sys
input=sys.stdin.readline
N=int(input())
card={}
l=list(map(int,input().split()))
for i in l:
    if i in card:card[i]+=1
    else: card[i]=1
M=int(input())
print(' '.join(map(lambda x:str(card[int(x)]) if int(x) in card else '0',input().split())))
