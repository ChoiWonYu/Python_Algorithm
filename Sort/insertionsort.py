import time
from random import randrange
a=[]
time_sum=0
for i in range(100000):
    a.append(randrange())
def insertionsort(A:[]):
    for i in range(1,len(A)):
        for j in range(i,0,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
            else:
                break
    return A

