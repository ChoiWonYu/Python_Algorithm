import sys
input=sys.stdin.readline
N=int(input())
card={}
l=input().split()
for i in l:
    if i in card:card[i]+=1
    else: card[i]=1
M=int(input())
S=input().split()
print(' '.join(str(card[x]) if x in card else '0' for x in S))
